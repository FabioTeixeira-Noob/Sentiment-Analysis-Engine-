from src.analyzer import analyze

def main():
    print("=== Sentiment Analysis Engine ===")
    text = input("Enter text to analyze: ")

    result = analyze(text)

    print("\n--- Analysis Result ---")
    print(f"Original text : {result['original_text']}")
    print(f"Cleaned text  : {result['cleaned_text']}")
    print(f"Sentiment     : {result['sentiment']}")
    print(f"Polarity score: {result['polarity']}")

if __name__ == "__main__":
    main()
