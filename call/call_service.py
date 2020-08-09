import requests



class service_call:
    def __init__(self, tweet):
        self.url = 'http://0.0.0.0:5000/sentiment'
        self.data = '''{"col" : ''' + '"' + tweet + '"' +'''}'''
        self.url2 = 'http://localhost:5000/textAnalytics'

    def call_service(self):
        response = requests.post(self.url, data=self.data)
        return response.json()

    def text_analytics(self):
        response = requests.post(self.url2, data=self.data)
        res_json = response.json()
        return str(res_json['Keywords']['keyPhrases'])

    def entity(self):
        response = requests.post(self.url2, data=self.data)
        res_json = response.json()
        details = (res_json['NER']['entities'])
        return (str(details))


# if __name__=="__main__":
#     tweet = "We went to Contoso Steakhouse located at midtown NYC last week for a dinner party, and we adore the spot! They provide marvelous food and they have a great menu. The chief cook happens to be the owner (I think his name is John Doe) and he is super nice, coming out of the kitchen and greeted us all. We enjoyed very much dining in the place! The Sirloin steak I ordered was tender and juicy, and the place was impeccably clean. You can even pre-order from their online menu at www.contososteakhouse.com, call 312-555-0176 or send email to order@contososteakhouse.com! The only complaint I have is the food didn't come fast enough. Overall I highly recommend it! "
#     obj = service_call(tweet)
#     obj.entity()
