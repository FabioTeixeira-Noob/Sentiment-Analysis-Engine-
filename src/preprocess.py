import re

def clean_text(text: str) -> str:
    """
    Cleans input text by:
    - Lowercasing
    - Removing URLs
    - Removing special characters
    - Removing extra spaces
    """
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
