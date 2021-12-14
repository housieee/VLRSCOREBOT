
import tweepy
ACCESS_KEY = '1464740045571645447-sIb4DezMIhutcCUp3N6k05rO8wVBpY'
ACCESS_SECRET = 'AzMcXoL2CSFqBMv3jo9JLn6KzIMbLM8KQbsw0UABMiyDr'
CONSUMER_KEY = 'meX5lyCdclUhWD9BB3DLQWJdP'
CONSUMER_SECRET = 'g9ULz6hYkVcwNxHjAmZ58P53UGliYJYgULBS1c3nTPm6cRzs4P'


api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAABQPWQEAAAAAgZvmIEBXYYNsVLuWbREOu9aiJZM%3DAY0yK5G1mQf30qVrWnOcagimfRlmaZrET7SWXfJPBeyMp1Wq0V',
                    access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET)

def tweet(matchscore):
    api.create_tweet(text=matchscore)