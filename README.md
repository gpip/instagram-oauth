## Usage

```
from instagram_oauth import InstagramOauthAPI

client = InstagramOauthAPI(
    client_id=<client id>,
    client_secret=<client secret>
    redirect_uri=<redirect uri>
)

# Build the authorization url.
url = client.auth_url()

# Forward the user to the url above and then check for a callback
# from Instagram to your server.
code = <code received>

# Grab the access token.
result = client.exchange_code_for_accesstoken(code)
print(result['access_token'])
print(result['user'])
```
