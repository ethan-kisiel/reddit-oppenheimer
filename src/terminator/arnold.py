from praw import Reddit
from os import environ
from .environment_vars import *

CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
USER_AGENT = environ.get('USER_AGENT')

class Arnold:
    '''
    houses the delete function for
    removing user comments and posts
    '''
    async def commence_deletion(username: str, password: str):
        args = {'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'user_agent': USER_AGENT,
                'username': username,
                'password': password}

        with Reddit(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    user_agent=USER_AGENT,
                    username=username,
                    password=password) as reddit:
            redditor = reddit.user.me()
            for comment in redditor.comments.new(limit=None):
                comment.delete()
            for post in redditor.submissions.new(limit=None):
                post.delete()