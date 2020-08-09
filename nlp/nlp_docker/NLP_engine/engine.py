from summarizer import Summarizer
from rake_nltk import Rake
import spacy
from spacy_langdetect import LanguageDetector
from nlp.nlp_docker.NLP_engine.language_encoding import lang_lookup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
rake = Rake()
summarizer = Summarizer()

class NLP_services:
    def __init__(self,body):
        self.body = body

    def get_summary(self):
        return {'result': summarizer(self.body)}

    def sentiment(self):
        return {'result': analyser.polarity_scores(self.body)['compound']}

    def text_analytics(self):

        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
        doc = nlp(self.body)

        language = dict()
        language['name'] = lang_lookup[doc._.language['language']]
        language['iso6391Name'] = doc._.language['language']
        language['probability'] = doc._.language['score']

        keywords = dict()
        rake.extract_keywords_from_text(self.body)
        keywords['keyPhrases'] = rake.get_ranked_phrases()

        tags = dict()
        tags['entities'] = [(X.text, X.label_) for X in doc.ents]

        sentiment = dict()
        sentence_sentiment = dict()
        sentences = self.body.split('. ')
        for sentence in sentences:
            sentence_sentiment[sentence] = analyser.polarity_scores(sentence)
        doc_sentiment = analyser.polarity_scores(self.body)
        sentiment['sentence_level_sentiment'] = sentence_sentiment
        sentiment['doc_level_sentiment'] = doc_sentiment

        return {'Language': language, 'Keywords': keywords, 'NER': tags, 'Seniment': sentiment}