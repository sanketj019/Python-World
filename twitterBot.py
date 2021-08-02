#You will need to PIP INSTALL tweepy for this to work and also create a twitter API.

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search1 = "subject you want to search and like the post related to it"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Follwer Name yo want to follow':
    print(follower.name)
    follower.follow()
    break
    


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search1).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Liked the tweet')
        break
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
