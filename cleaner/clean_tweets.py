from nltk import word_tokenize
from nltk.corpus import stopwords
import re #regular expressionfrom textblob import TextBlob
import string

emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])

emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])



emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)
class tweeclean:
    def __init__(self,tweet):
        self.tweet = tweet

    def clean_tweets(self):
        emoticons = emoticons_happy.union(emoticons_sad)
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(
            self.tweet)  # after tweepy preprocessing the colon symbol left remain after      #removing mentions
        self.tweet = re.sub(r':', '', self.tweet)
        self.tweet = re.sub(r'‚Ä¶', '', self.tweet)
        # replace consecutive non-ASCII characters with a space
        self.tweet = re.sub(r'[^\x00-\x7F]+', ' ', self.tweet)  # remove emojis from tweet
        self.tweet = emoji_pattern.sub(r'', self.tweet)  # filter using NLTK library append it to a string
        filtered_tweet = [w for w in word_tokens if not w in stop_words]
        filtered_tweet = []  # looping through conditions
        for w in word_tokens:
            # check tokens against stop words , emoticons and punctuations
            if w not in stop_words and w not in emoticons and w not in string.punctuation:
                filtered_tweet.append(w)
        return ' '.join(filtered_tweet)