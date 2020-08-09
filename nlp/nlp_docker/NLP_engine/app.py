#Import libraries
from flask import Flask, request, Response
from nlp.nlp_docker.NLP_engine.engine import NLP_services
import json
app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    details = json.loads(request.data.decode('utf-8'), strict=False)
    obj = NLP_services(details['col'])
    return Response(json.dumps(obj.get_summary(), indent=1))

@app.route('/textAnalytics', methods=['GET', 'POST'])
def textAnalytics():
    details = json.loads(request.data.decode('utf-8'), strict=False)
    obj = NLP_services(details['col'])
    return Response(json.dumps(obj.text_analytics(), indent=1))

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    details = json.loads(request.data.decode('utf-8'), strict=False)
    obj = NLP_services(details['col'])
    return Response(json.dumps(obj.sentiment(), indent=1))


if __name__ == '__main__':
    app.run(host='0.0.0.0')


