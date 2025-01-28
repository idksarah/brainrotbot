import os
import configparser
import praw
from praw.models import MoreComments
from tts import create_voice_over

config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(
    client_id=os.getenv('reddit_id'),
    client_secret=os.getenv('reddit_secret'),
    user_agent=config['Reddit']['USER_AGENT']
)

# get comment content
def addComment(comment):
    id = comment.id
    text = comment.body
    print(text)
    create_voice_over(id, text)

def getContentFromPost(submission):
    submission.coment_sort = "top"
    submission.comment_limit = 1
    submissionComments = submission.comments
    for comment in submissionComments:
        if isinstance(comment, MoreComments):
            continue
        if(len(comment.body.split()) > 60):
            continue
        addComment(comment)

for submission in reddit.subreddit("askReddit").hot(limit=None):
    if(submission.over_18):
        continue
    
    print(submission.title)
    break

getContentFromPost(submission)