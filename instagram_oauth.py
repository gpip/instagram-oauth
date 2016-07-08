import requests


class OAuth2AuthExchangeError(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


class InstagramOauthAPI:

    instagram_url = 'https://www.instagram.com'
    oauth_base_url = 'https://api.instagram.com/oauth'

    def __init__(self, client_id, client_secret, redirect_uri=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def auth_url(self, scope=None, response_type='code'):
        """Build the authorization url."""
        data = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': response_type,
            'scope': ' '.join(scope or [])
        }
        url = '%s/authorize' % self.oauth_base_url
        req = requests.Request('GET', url, params=data)
        prepared = req.prepare()
        return prepared.url

    def get_browser_auth_url(self, authurl):
        """
        Helper for returning a final url that can be copied & pasted
        into a browser for requesting user authorization.
        """
        req = requests.get(authurl)
        status = req.status_code
        if status != 200:
            raise OAuth2AuthExchangeError(
                "The server returned a non-200 response (%d) for URL %s" % (
                    status, authurl))
        redirected_to = req.url
        return redirected_to

    def exchange_code_for_accesstoken(self, code):
        """Send a request to obtain an access token."""
        data = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        req = requests.post('%s/access_token' % self.oauth_base_url, data=data)
        status = req.status_code
        result = req.json()
        if status != 200:
            raise OAuth2AuthExchangeError(result.get("error_message", ""))
        return result


if __name__ == "__main__":
    import json
    client_id = raw_input("Client ID: ").strip()
    client_secret = raw_input("Client Secret: ").strip()
    redirect_uri = raw_input("Redirect URI: ").strip()
    raw_scope = raw_input("Requested scope (separated by spaces, blank for just basic read): ").strip()
    scope = raw_scope.split(' ')

    client = InstagramOauthAPI(
            client_id=client_id, client_secret=client_secret,
            redirect_uri=redirect_uri)
    url = client.auth_url(scope=scope)
    print "Visit this page and grant access: %s" % url

    code = raw_input("Paste in code in query string after redirect: ").strip()
    result = client.exchange_code_for_accesstoken(code)
    print "\nSuccess!\nAccess token: %s\nUser: %s" % (
            result['access_token'], json.dumps(result['user'], indent=2))
