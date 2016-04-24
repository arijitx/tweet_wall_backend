import tweepy
import sys
from textblob import TextBlob
import time
import json
#override tweepy.StreamListener to add logic to on_status



CONSUMER_KEY = 'jrkcjINAfIEqoGpQ7tb13DIhk'
CONSUMER_SECRET = 'AXval8wJ4f0GKlYAUGsx9TgGOOZNUf24Z37ROpmdZ833h584gi'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '558579036-xm8Nav9bQ82difJgpDkbMIWzeKrgCASz9P5fkzjV'#keep the quotes, replace this with your access token
ACCESS_SECRET = '2uKoxZGiGqIynj7B4tUsN0YIrSLvyCbLo1sijqUsmEM7j'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
sentiment_score=0
count=0
tpm=0
q=''
ana={}
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        global count
        global sentiment_score
        global tps
        global ana
        global q
        count+=1
        blob=TextBlob(status.text)
        sent=0
        print status.text
        for sentence in TextBlob(status.text).sentences:
          sent+=sentence.sentiment.polarity
        sentiment_score+=sent
        sentiment_score/=count
        tps=(count/(time.time()-t))*60
        ana["sentiment_score"]=sentiment_score
        ana["count"]=count
        ana["tps"]=tps
        ana["tag"]='#'+q
        with open("analytics.json", "w") as outfile:
            json.dump(ana, outfile, indent=4)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


q=str(sys.argv[1])
t=time.time()
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['#'+q])