import json
import drink



def verifyDrinkRequest(tweet_text, tweet_json):
  tweet_user = tweet_json['user']['screen_name']
  keyCount = 0

  if 'RT' not in tweet_text:

    for keyword in keywords:
      
      if keyword in tweet_text.lower():
        ingredient = keyword.replace('#','')
        drinkData  = drink.getDrinkData(ingredient)

        userSignature = "Hey!, @{}\n".format(tweet_user)
        message = drinkData['message']

        print(userSignature+message)        
        break

      else:

        keyCount += 1
        if keyCount == 5:
          print("Couldn't find an ingredient I know :(")

  else:

    print("Ignored, just a re-tweet")  


tweet_text = 'Q pedo @BartendBot que esta bueno con #rum! tequila!'
tweet_json = {'created_at': 'Fri Apr 10 19:39:22 +0000 2020', 'id': 1248697098985443329, 'id_str': '1248697098985443329', 'text': 'Q pedo @BartendBot que esta bueno con vodka!', 'source': '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>', 'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 1158090065849044999, 'id_str': '1158090065849044999', 'name': 'flunkout_dvlpr', 'screen_name': 'flunkout_dvlpr', 'location': 'Houston, TX', 'url': None, 'description': 'flunkout to fullStack Developer', 'translator_type': 'none', 'protected': False, 'verified': False, 'followers_count': 0, 'friends_count': 1, 'listed_count': 0, 'favourites_count': 7, 'statuses_count': 8, 'created_at': 'Sun Aug 04 18:59:22 +0000 2019', 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': '', 'profile_background_image_url_https': '', 'profile_background_tile': False, 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1158558925630914560/aFIYMLPR_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1158558925630914560/aFIYMLPR_normal.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1158090065849044999/1565057370', 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'quote_count': 0, 'reply_count': 0, 'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [], 'urls': [], 'user_mentions': [{'screen_name': 'BartendBot', 'name': 'Bartend Bot', 'id': 1248456843971592196, 'id_str': '1248456843971592196', 'indices': [7, 18]}], 'symbols': []}, 'favorited': False, 'retweeted': False, 'filter_level': 'low', 'lang': 'es', 'timestamp_ms': '1586547562725'}
keywords = [ '#gin', '#rum', '#scotch', '#tequila', '#vodka']
verifyDrinkRequest(tweet_text, tweet_json)


  # if 'RT' not in tweet_text:
  #   if 'tequila' in tweet_text.lower():
  #     print("Tequila Request! by: @", tweet_user)
  #     data = drink.getTweetData('tequila')
  #     userSignature = "Hey!, @{}\n".format(tweet_user)
  #     api.update_status(status = userSignature+data['message']) 
  #   elif 'vodka' in tweet_text.lower():
  #     print("Vodka Request! by: @", tweet_user)
  #     data = drink.getTweetData('vodka')
  #     userSignature = "Hey!, @{}\n".format(tweet_user)
  #     api.update_status(status = userSignature+data['message']) 
  #   elif 'gin' in tweet_text.lower():
  #     print("Gin Request! by: @", tweet_user)
  #     data = drink.getTweetData('gin')
  #     userSignature = "Hey!, @{}\n".format(tweet_user)
  #     api.update_status(status = userSignature+data['message']) 
  #   elif 'gin' in tweet_text.lower():
  #     print("Gin Request! by: @", tweet_user)
  #     data = drink.getTweetData('gin')
  #     userSignature = "Hey!, @{}\n".format(tweet_user)
  #     api.update_status(status = userSignature+data['message']) 
  #   elif 'rum' in tweet_text.lower():
  #     print("Rum Request! by: @", tweet_user)
  #     data = drink.getTweetData('rum')
  #     userSignature = "Hey!, @{}\n".format(tweet_user)
  #     api.update_status(status = userSignature+data['message']) 