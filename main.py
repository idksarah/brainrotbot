import os
import configparser
import praw

# read/set environment and praw variables
config = configparser.ConfigParser()
config.read('config.ini')

# new reddit instance
reddit = praw.Reddit(
    client_id=os.getenv('reddit_id'),
    client_secret=os.getenv('reddit_secret'),
    user_agent=config['Reddit']['USER_AGENT']
)

print(reddit.read_only)

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)