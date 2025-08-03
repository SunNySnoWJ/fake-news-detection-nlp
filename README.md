# Fake News Detection using BERT and Adversarial Robustness Testing

This project applies BERT-based models to detect fake news and further evaluates their robustness against adversarial attacks using **TextFooler**. It covers preprocessing, training, evaluation, adversarial training, and post-attack analysis with visualizations.

## Project Structure

fake-news-detection-nlp/
├── Code/
│   ├── model_bert.ipynb            # Main notebook for training and evaluation
│   ├── Preprocessing_Fakenewsnet.py
│   ├── Preprocessing_Latest_News.py
│   └── realtime_news.py
├── dataset/
│   ├── *
│   └── Fakenewsnet/
│       ├── politifact_fake.csv
│       ├── politifact_real.csv
│       ├── gossipcop_fake.csv
│       └── gossipcop_real.csv
├── Result photos/
│   └── [charts, metrics, outputs].png
├── models/
│   └── *                # Saved models (after training)
├── Dataset Sources.txt             # Reference links to raw datasets
└── README.md


## How to Run

