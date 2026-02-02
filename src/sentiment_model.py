from textblob import TextBlob

def predict_sentiment(text: str):
    """
    Predicts sentiment using TextBlob polarity score
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.05:
        sentiment = "Positive"
    elif polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, round(polarity, 3)
