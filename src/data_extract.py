import tweepy
import pandas as pd
import preprocessor as p
import nltk
from cleaner.clean_tweets import tweeclean
from call import call_service


class data_extract:
    # Credentials-
    CONSUMER_KEY = 'PZFJ5OW0LaUXlfTsOxaN9aO4d'
    CONSUMER_SECRET = '9hMbQYK3ArpJTR4GDojiKmvMQPXcfN2enAD2OjdK6duYiHHHpC'
    ACCESS_TOKEN = '465665764-V7cme9ohdFVUBI2jqjXEK9lMZnzDpVl97AFVGMVW'
    ACCESS_TOKEN_SECRET = "dP6AFK7v2tOE7LTNHRgNVMJtCzpZWv2cA1DczXTKLyMPQ"

    def __init__(self, name, records):
        self.screen_name = name
        self.number_records = records
        self.tweets_obj = []
        self.tweet_list = []
        self.cleaned_text = []
        self.clear_text = []
        self.key_phrase = []
        self.entities = []

    def authentication(self):
        # Authentication
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name=self.screen_name, count = int(self.number_records))
        self.tweets_obj.extend(new_tweets)
        for i in self.tweets_obj:
            self.tweet_list.append(i.text)
        return(pd.DataFrame(self.tweet_list, columns=["tweets_text"]))

    def clean(self, tweet_df):
        #forming a separate feature for cleaned tweets.
        for i in self.tweet_list:
            clean = p.clean(i)
            self.cleaned_text.append(clean)

        for i in self.cleaned_text:
            tweetclean = tweeclean(i)
            self.clear_text.append(tweetclean.clean_tweets())
        tweet_df['cleaned_text'] = self.clear_text
        return tweet_df

# tweets.to_csv("/home/webhav/Documents/sentiment_analysis/analysis/tweets.csv")

    def sentiment_analysis(self, tweet_df):
        sentiments = []
        sentiment_score = []
        for i in self.clear_text:
            call_serv = call_service.service_call(i)
            senti_score = call_serv.call_service()
            sentiment_score.append(senti_score["result"])
            if senti_score["result"] < 0:
                senti = "Negative"
            elif senti_score["result"] == 0.0:
                senti = "Neutral"
            elif senti_score["result"] > 0:
                senti = "Positive"
            sentiments.append(senti)
        tweet_df['sentiments'] = sentiments
        return tweet_df

    def key_phrases(self, tweets_df):
        for i in self.clear_text:
            call_serv = call_service.service_call(i)
            imp_phrases = call_serv.text_analytics()
            self.key_phrase.append(imp_phrases)
        tweets_df['imp_phrases'] = self.key_phrase
        return tweets_df

    def get_entities(self, tweets_df):
        for i in self.clear_text:
            call_serv = call_service.service_call(i)
            imp_entity = call_serv.entity()
            self.entities.append(imp_entity)
        print(self.entities)
        tweets_df['entities'] = self.entities
        return tweets_df


if __name__=="__main__":
    extraxt_obj = data_extract('@CRMNEXT', 5)
    tweet_df = extraxt_obj.authentication()
    tweet_df = extraxt_obj.clean(tweet_df)
    tweet_df = extraxt_obj.sentiment_analysis(tweet_df)
    tweet_df = extraxt_obj.key_phrases(tweet_df)
    tweet_df = extraxt_obj.get_entities(tweet_df)
    print(tweet_df)
    tweet_df.to_csv("/home/webhav/Documents/sentiment_analysis/analysis/sentiments_alaysis.csv")
