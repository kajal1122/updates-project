from flask import Flask,render_template,request
import feedparser

app=Flask(__name__)
FEED_URLS ={"whowhatwear":"http://feeds.bbci.co.uk/news/rss.xml",
            "fm":"https://fashionmagazine.com/feed/",
            "gqmen":"https://www.gq.com/feed/style/rss"}
@app.route('/')
def home():
    query = request.args.get("magazine")
    if not query or query.lower() not in  FEED_URLS:
        magazine = "whowhatwear"
    else:
        magazine = query.lower()

    feed = feedparser.parse(FEED_URLS[magazine])
    articles = feed["entries"]
    return render_template('home.html',articles=articles)


if __name__ =='__main__':
    app.run(debug=True)
