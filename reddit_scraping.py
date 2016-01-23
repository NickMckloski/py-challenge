import praw

r = praw.Reddit(user_agent='Test Script')
submissions = r.get_subreddit('dailyprogrammer').get_hot()
for submission in submissions:
    print(submission.title)
