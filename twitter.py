import config
import tweepy


api = tweepy.Client(bearer_token=config.BT,
                    access_token=config.AK,
                    access_token_secret=config.AS,
                    consumer_key=config.CK,
                    consumer_secret=config.CS)

def tweet(matchscore):
    api.create_tweet(text=matchscore)

