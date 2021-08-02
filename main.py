from flask  import Flask, request, render_template
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

app = Flask(__name__)
@app.route("/")

@app.route("/index.html", methods=["POST","GET"])
def sentimentanalysis():
    text = ""
    if request.method == "POST":
        text = request.form['text']
        polarity, subjectivity = TextBlob(text).sentiment
        blob = TextBlob(text)
        blob.sentiment
        sid = SentimentIntensityAnalyzer()
        sid.polarity_scores(text)
        result = ""
        if polarity>0:
            result = "Positive"
        elif polarity<0:
            result = "Negative"
        else:
            result = "Neutral"
            
        return render_template("index.html",
            text = text,
            confidence = round(abs(polarity*100)),
            result = result, final=blob.sentiment, score=sid.polarity_scores(text))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
