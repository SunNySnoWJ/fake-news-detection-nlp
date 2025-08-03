"""
Script: Latest_News_Preprocessing.py
Description: Preprocess latest news data for fake news detection.
Input: dataset/latest_news.csv
Output: dataset/cleaned_latest_news.csv
"""

import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Download required NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Clean a single text input
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)                     # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)                 # Remove punctuation & numbers
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words and len(w) > 2]
    return " ".join(tokens)

# Apply full preprocessing pipeline to the dataset
def preprocess_latest_news(df):
    df['clean_title'] = df['title'].apply(clean_text)

    if 'content' in df.columns:
        df['clean_text'] = df['content'].apply(clean_text)
        df['text_len'] = df['clean_text'].apply(lambda x: len(x.split()))
        df['text_sentiment'] = df['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    else:
        df['text_len'] = df['clean_title'].apply(lambda x: len(x.split()))
        df['text_sentiment'] = df['clean_title'].apply(lambda x: TextBlob(x).sentiment.polarity)

    if 'publishedAt' in df.columns:
        df['publish_date'] = pd.to_datetime(df['publishedAt'], errors='coerce')
        df['publish_year'] = df['publish_date'].dt.year
        df['publish_month'] = df['publish_date'].dt.month

    return df

# Main execution
if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(__file__))
    input_path = os.path.join(base_dir, "dataset", "latest_news.csv")
    output_path = os.path.join(base_dir, "dataset", "cleaned_latest_news.csv")

    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)

    print("Available columns:", df.columns.tolist())
    print(df.head())

    df_cleaned = preprocess_latest_news(df)

    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")
    print(df_cleaned[['clean_title', 'text_len', 'text_sentiment']].head())
