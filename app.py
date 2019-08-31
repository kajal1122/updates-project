from flask import Flask,render_template,request
import json
import feedparser
import urllib.parse,urllib.request




app=Flask(__name__)
FEED_URLS ={"whowhatwear":"http://feeds.bbci.co.uk/news/rss.xml",
            "fm":"https://fashionmagazine.com/feed/",
            "gqmen":"https://www.gq.com/feed/style/rss"}
@app.route('/')
def home():
    query = request.args.get("magazine")
    weather = get_weather(request.args.get("weather"))
    if not query or query.lower() not in  FEED_URLS:
        magazine = "whowhatwear"
    else:
        magazine = query.lower()

    feed = feedparser.parse(FEED_URLS[magazine])
    articles = feed["entries"]

    return render_template('home.html',articles=articles,weather=weather)


def get_weather(query):
    weather_api= "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=037e412d25a08b9c27d0a1756a91b171"
    #query = urllib.parse.quote(query)
    weather_api=weather_api.format(query)
    data = urllib.request.urlopen(weather_api).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {
                "description": parsed['weather'][0]['description'],
                "temperature": parsed['main']['temp'],
                "city":parsed['name'],
                "country":parsed['sys']['country'],

                    }
    return weather




if __name__ =='__main__':
    app.run(debug=True)
