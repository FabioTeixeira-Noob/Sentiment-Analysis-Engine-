from src.preprocess import clean_text
from src.sentiment_model import predict_sentiment

def analyze(text: str) -> dict:
    """
    Full sentiment analysis pipeline
    """
    cleaned_text = clean_text(text)
    sentiment, polarity = predict_sentiment(cleaned_text)

    return {
        "original_text": text,
        "cleaned_text": cleaned_text,
        "sentiment": sentiment,
        "polarity": polarity
    }
