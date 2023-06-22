# Chap02/twitter_client.py
#import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = getTokenFromFile("APIKey.txt")
        consumer_secret = getTokenFromFile("APIKeySecret.txt")
        access_token = getTokenFromFile("AccessToken.txt")
        access_secret = getTokenFromFile("AccessTokenSecret.txt")

    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    print("Auth: ", auth)
    print("Client: ", client)
    return client

get_twitter_client()
