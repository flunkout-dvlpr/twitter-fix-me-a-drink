import tweepy
import json
import twitterKeys
import time
import drink

consumer_key        = twitterKeys.apiKey
consumer_secret     = twitterKeys.apiSecret
access_token        = twitterKeys.accessToken
access_token_secret = twitterKeys.accessSecret
  
# authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)   
api = tweepy.API(auth) 


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

  def on_status(self, status):
    tweet_text = status.text
    tweet_json = status._json
    
    print(tweet_text)
    print(tweet_json)

    tweet_user = tweet_json['user']['screen_name']

    if 'RT' not in tweet_text:
      if 'tequila' in tweet_text.lower():
        print("Tequila Request! by: @", tweet_user)
        data = drink.getTweetData('tequila')
        userSignature = "Hey!, @{}\n".format(tweet_user)
        api.update_status(status = userSignature+data['message']) 
      elif 'vodka' in tweet_text.lower():
        print("Vodka Request! by: @", tweet_user)
        data = drink.getTweetData('vodka')
        userSignature = "Hey!, @{}\n".format(tweet_user)
        api.update_status(status = userSignature+data['message']) 
      elif 'gin' in tweet_text.lower():
        print("Gin Request! by: @", tweet_user)
        data = drink.getTweetData('gin')
        userSignature = "Hey!, @{}\n".format(tweet_user)
        api.update_status(status = userSignature+data['message']) 
      elif 'gin' in tweet_text.lower():
        print("Gin Request! by: @", tweet_user)
        data = drink.getTweetData('gin')
        userSignature = "Hey!, @{}\n".format(tweet_user)
        api.update_status(status = userSignature+data['message']) 
      elif 'rum' in tweet_text.lower():
        print("Rum Request! by: @", tweet_user)
        data = drink.getTweetData('rum')
        userSignature = "Hey!, @{}\n".format(tweet_user)
        api.update_status(status = userSignature+data['message']) 


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@botrhebartender'])

