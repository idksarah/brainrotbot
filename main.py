import os
import configparser
import praw
from praw.models import MoreComments

# read/set environment and praw variables
config = configparser.ConfigParser()
config.read('config.ini')

# new reddit instance
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

def getContentFromPost(submission):
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        if(len(comment.body.split()) > 60):
            continue
        addComment(comment)

for submission in reddit.subreddit("askReddit").hot(limit=1):
    if(submission.over_18):
        continue
    getContentFromPost(submission)