from asyncpraw import Reddit
from asyncpraw.exceptions import *

USER_AGENT = '<web:OPPENHEIMER:1.0>'

class Arnold:
    '''
    houses the delete function for
    removing user comments and posts
    '''
    async def commence_deletion(
            client_id: str,
            client_secret: str,
            username: str, password: str):
        
        with Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=USER_AGENT,
                username=username,
                password=password) as reddit:
            
            try:
                redditor = await reddit.user.me()
            except Exception as e:
                return "Couldn't instantiate user."
            try:
                async for comment in redditor.comments.new(limit=None):
                    await comment.delete()
            except Exception as e:
                print(e)
                return "Couldn't delete comments."
            try:
                async for post in redditor.submissions.new(limit=None):
                    await post.delete()
            except Exception as e:
                print(e)
                return "Couldn't delete posts."
            return None