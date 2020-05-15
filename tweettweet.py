import tweepy
import time

auth = tweepy.OAuthHandler('xxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
auth.set_access_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'xxxxxxxx':
        follower.follow()
        break

# print(user.followers_count)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('twitter')
# print(user.screen_name)
# print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
