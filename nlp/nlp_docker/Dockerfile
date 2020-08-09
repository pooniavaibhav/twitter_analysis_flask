FROM python:3.6

COPY . /src/app

WORKDIR /src/app

ENV PYTHONPATH "${PYTHONPATH}:/src/app"

RUN python3 -m pip install -U numpy

RUN python3 -m pip install -U nltk

RUN python3 -c "import nltk; nltk.download('stopwords')"

RUN python3 -m pip install rake-nltk

RUN python3 -m pip install -r req.txt

RUN python3 -m pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

CMD ["python", "NLP_engine/app.py"]
