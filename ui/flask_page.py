from flask import Flask, render_template,url_for, redirect, request
from ui.forms import SearchForm
from src.data_extract import data_extract
#__name__ is the special variable in python that has tha name of the module.
#This is done so that you flask know where to look for you templates and static files.

app = Flask(__name__)
app.config['SECRET_KEY'] = '8acf8cf5d43f5d3edf93f2f9a433f640'


#route-A route is what we write into the browser to go to different pages. so here we do through route decorators.
# so this forward slash is the root/home page of our website.
@app.route("/", methods = ['GET','POST'])
def register():
    form = SearchForm()
    if form.submit():
        twitter = form.twitter_handle.data
        count = form.count.data
        if twitter:
            extraxt_obj = data_extract(twitter, count)
            tweet_df = extraxt_obj.authentication()
            tweet_df = extraxt_obj.clean(tweet_df)
            tweet_df = extraxt_obj.sentiment_analysis(tweet_df)
            tweet_df = extraxt_obj.key_phrases(tweet_df)
            tweet_df = extraxt_obj.get_entities(tweet_df)
            print(tweet_df)
            tweet_df.to_csv("/home/webhav/Documents/sentiment_analysis/analysis/sentiments_alaysis.csv")
            return redirect(url_for('about'))
    return render_template('search.html', title = 'search', form = form)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

def analysis(twitter, count):
    extraxt_obj = data_extract(twitter, count)
    tweet_df = extraxt_obj.authentication()
    tweet_df = extraxt_obj.clean(tweet_df)
    tweet_df = extraxt_obj.sentiment_analysis(tweet_df)
    tweet_df = extraxt_obj.key_phrases(tweet_df)
    tweet_df = extraxt_obj.get_entities(tweet_df)
    print(tweet_df)
    tweet_df.to_csv("/home/webhav/Documents/sentiment_analysis/analysis/sentiments_alaysis.csv")