from setuptools import setup

setup(
    name="instagram-oauth",
    version="0.1",
    description='Instagram API oauth authentication helper',
    long_description=open('README.md').read(),
    url='https://github.com/gpip/instagram-oauth',
    author='Guilherme Polo',
    author_email='gp@luster.cc',
    setup_requires=['requests'],
    install_requires=['requests'],
    py_modules=['instagram_oauth'],
    keywords=['instagram', 'oauth', 'api'],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries"
    ]
)
