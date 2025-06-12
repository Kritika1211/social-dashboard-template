import tweepy

def get_twitter_api(token):
    auth = tweepy.OAuth1UserHandler("CONSUMER_KEY", "CONSUMER_SECRET", token, "ACCESS_TOKEN_SECRET")
    return tweepy.API(auth)

def fetch_tweets(api):
    return api.home_timeline(count=5)

def post_tweet(api, content):
    return api.update_status(content)