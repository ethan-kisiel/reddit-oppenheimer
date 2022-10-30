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
                print(e)
                return "Couldn't instantiate user."
            try:
                # get user comments and unwrap MoreComments object
                comments = redditor.comments.new(limit=None)
                #await comments.replace_more(limit=None)
                async for comment in comments:
                    await comment.delete()
            except Exception as e:
                print(e)
                return "Couldn't delete comments."
            try:
                # get all redditor posts
                posts = redditor.submissions.new(limit=None)
                async for post in posts:
                    await post.delete()
            except Exception as e:
                print(e)
                return "Couldn't delete posts."
            return None