"""
Script: fakenewsnet_preprocessing.py
Description: Preprocess FakeNewsNet dataset files and output cleaned CSVs.
Input: dataset/FakeNewsNet/*/*.csv
Output: dataset/cleaned_fakenewsnet.csv
"""

import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Clean a single text input
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words and len(w) > 2]
    return " ".join(tokens)

# Process one file and return cleaned dataframe
def preprocess_fakenewsnet_csv(file_path):
    df = pd.read_csv(file_path)

    if 'title' in df.columns:
        df['clean_title'] = df['title'].apply(clean_text)
    else:
        df['clean_title'] = ""

    if 'text' in df.columns:
        df['clean_text'] = df['text'].apply(clean_text)
        df['text_len'] = df['clean_text'].apply(lambda x: len(x.split()))
        df['text_sentiment'] = df['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    else:
        df['text_len'] = df['clean_title'].apply(lambda x: len(x.split()))
        df['text_sentiment'] = df['clean_title'].apply(lambda x: TextBlob(x).sentiment.polarity)

    if 'date' in df.columns:
        df['publish_date'] = pd.to_datetime(df['date'], errors='coerce')
        df['publish_year'] = df['publish_date'].dt.year
        df['publish_month'] = df['publish_date'].dt.month

    return df

# Main function to batch process all CSVs
if __name__ == "__main__":
    input_dir = os.path.join("dataset", "FakeNewsNet")
    output_path = os.path.join("dataset", "cleaned_fakenewsnet.csv")

    all_cleaned = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".csv"):
                csv_path = os.path.join(root, file)
                print(f"Processing: {csv_path}")
                df_cleaned = preprocess_fakenewsnet_csv(csv_path)
                all_cleaned.append(df_cleaned)

    if all_cleaned:
        merged_df = pd.concat(all_cleaned, ignore_index=True)
        merged_df.to_csv(output_path, index=False)
        print(f"Cleaned FakeNewsNet data saved to: {output_path}")
        print(merged_df[['clean_title', 'text_len', 'text_sentiment']].head())
    else:
        print("No CSV files found to process.")