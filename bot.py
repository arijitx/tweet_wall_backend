import tweepy
import time
import sys
import json
from textblob import TextBlob

CONSUMER_KEY = 'jrkcjINAfIEqoGpQ7tb13DIhk'
CONSUMER_SECRET = 'AXval8wJ4f0GKlYAUGsx9TgGOOZNUf24Z37ROpmdZ833h584gi'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '558579036-xm8Nav9bQ82difJgpDkbMIWzeKrgCASz9P5fkzjV'#keep the quotes, replace this with your access token
ACCESS_SECRET = '2uKoxZGiGqIynj7B4tUsN0YIrSLvyCbLo1sijqUsmEM7j'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

qu=str(sys.argv[1])
limit=int(sys.argv[2])
resp=[]
tw={}
res=tweepy.Cursor(api.search, q=qu,count=limit).items(limit)
for tweet in res:
    tw={}
    sent=0
    for sentence in TextBlob(tweet.text).sentences:
      sent+=sentence.sentiment.polarity
    tw["time"]=str(tweet.created_at)
    tw["text"]=tweet.text
    tw["lang"]=tweet.lang 
    tw["name"]=tweet.author.screen_name
    #tw["author_url"]=tweet.author.url
    tw["sentiment_score"]=sent
    tw["location"]=tweet.author.location
    tw["prof_img"]=tweet.author.profile_image_url
    resp.append(tw)


with open("response.json", "w") as outfile:
    json.dump(resp, outfile, indent=4)
outfile.close()