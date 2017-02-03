import twitter, env

api = twitter.Api(consumer_key=env.TWITTER_CKEY,
                  consumer_secret=env.TWITTER_CSECRET,
                  access_token_key=env.TWITTER_TKEY,
                  access_token_secret=env.TWITTER_TSECRET)

def tweet(msg):
    api.PostUpdate(msg)



