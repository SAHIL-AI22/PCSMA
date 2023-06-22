# Chap04/facebook_get_friends.py
import os
import facebook
import json
def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()

if __name__ == '__main__':
    #token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    token = getTokenFromFile('token.txt')
    graph = facebook.GraphAPI(token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"],"friends")
    #list = [friend['name'] for friend in friends['data']]
    print(json.dumps(friends, indent=4))