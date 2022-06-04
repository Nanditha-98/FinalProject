from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'GMvIILQk53H8sBfB64uqhXsQ9'
consumer_secret = 'a0IsO3YNgqj2TkRlZSZHmrpt2t8FCZJMLChLFfODV9mYEaT2Pn'
access_token = '1508307235482439680-yJrMuSCUFvO548ca3QSrg0KFqj4yQz'
access_secret = 'GSwExo5WI0sEixIWL2ec01IhXNxDl84P12AETtc9Kw5Cv'

class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])
