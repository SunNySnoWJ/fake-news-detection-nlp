# Fake News Detection Using BERT with Adversarial Robustness Testing

This project applies BERT-based models to detect fake news and further evaluates their robustness against adversarial attacks using TextFooler. It covers preprocessing, training, evaluation, adversarial training, and post-attack analysis with visualizations.

## Project Structure

```bash
fake-news-detection-nlp/
├── Code/
│   ├── model_bert.ipynb              # Main notebook for training and evaluation
│   ├── Preprocessing_Fakenewsnet.py  # Script to clean Fakenewsnet
│   ├── Preprocessing_Latest_News.py  # Script to clean real-time collected news
│   └── realtime_news.py              # Script to get real-time news from RSS
├── dataset/
│   └── Fakenewsnet/
│       ├── politifact_fake.csv
│       ├── politifact_real.csv
│       ├── gossipcop_fake.csv
│       └── gossipcop_real.csv
├── models/                           # Saved model directories (e.g. bert_model, bert_model_adversarial)
├── Result photos/                    # Visualization outputs (e.g. metrics, confusion matrix)
│   └── *.png
├── Dataset Sources.txt               # Reference links to raw datasets
└── README.md                         # Project documentation
```

## How to Run

1. Install Dependencies

Create a virtual environment (optional but recommended):
```bash
  python -m venv venv
  source venv/bin/activate    # or .\venv\Scripts\activate on Windows
```
Install required packages:
```bash
  pip install -r requirements.txt
```
2. Prepare Dataset
   
Run the following preprocessing scripts in order from the Code/ directory:
```bash
  python Preprocessing_Fakenewsnet.py
  python Preprocessing_Latest_News.py
  python realtime_news.py
```
3. Train and Evaluate the Models

Run the notebook:
```bash
  jupyter notebook model_bert.ipynb
```
Or convert and run as a Python script:
```bash
  jupyter nbconvert --to script model_bert.ipynb
  python model_bert.py
```
## Results & Outputs

After training and evaluation, the following results are expected:

Model Evaluation
	•	Classification Report showing precision, recall, and F1-score
	•	Confusion Matrix heatmap for Fake vs Real predictions

Adversarial Testing
	•	TextFooler attack applied before and after adversarial training
	•	Significant reduction in attack success rate after retraining
	•	Visualizations include:
	•	Bar chart of attack success vs resistance
	•	Histogram of prediction confidence scores

Prediction Results
	•	Clean news predictions:
	•	dataset/bert_predictions_on_cleaned_news.csv
	•	Predictions with confidence:
	•	dataset/bert_predictions_with_confidence.csv

Output Visualizations
All key result figures (metrics, plots, etc.) are stored in:
  Result photos/
  
This includes:
	•	Confusion matrix screenshot
	•	Attack performance plots
	•	Confidence distribution visualizations
