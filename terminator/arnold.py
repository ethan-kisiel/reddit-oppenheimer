from asyncpraw import Reddit
from asyncpraw.models import Redditor
from asyncpraw.exceptions import *

USER_AGENT = '<web:OPPENHEIMER:1.0>'

class Arnold:
    '''
    houses the delete function for
    removing user comments and posts
    '''
    async def delete_comments(redditor: Redditor, threshold: int):
        try:
            # get user comments and unwrap MoreComments object
            comments = redditor.comments.new(limit=None)
            #await comments.replace_more(limit=None)
            
            #Should this be an async for loop?
            async for comment in comments:
                # if there is no threshold, comment is deleted
                # else delete only if comment score is below threshold
                
                if threshold is not None:
                    await comment.delete()
                elif comment.score < threshold:
                    await comment.delete()

        except Exception as e:
            print(e)
            return "Couldn't delete comments."
        
    async def delete_posts(redditor: Redditor, threshold: int):
        try:
            # get all redditor posts
            posts = redditor.submissions.new(limit=None)
            # Shold this be an async for loop?
            async for post in posts:
                if threshold is not None:
                    await post.delete()
                elif post.score < threshold:
                    await post.delete()
        except Exception as e:
            print(e)
            return "Couldn't delete posts."

    async def commence_deletion(client_id: str,
                                client_secret: str,
                                username: str,
                                password: str,
                                threshold = None):

        if threshold is not None:
            threshold = int(threshold)

        reddit = Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=USER_AGENT,
                        username=username,
                        password=password)

        try:
            redditor = await reddit.user.me()
        except Exception as e:
            print(e)
            return "Couldn't instantiate user."
        
        comments_result = await Arnold.delete_comments(redditor, threshold)
        if comments_result:
            return comments_result

        posts_result = await Arnold.delete_posts(redditor, threshold)
        if posts_result:
            return posts_result
        
        try:
            await reddit.close()
        except Exception as e:
            print(e)
            return "An error occured when closing the session"

        return None
        
        