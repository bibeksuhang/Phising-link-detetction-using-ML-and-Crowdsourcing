import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import warnings
import kagglehub
import nltk

from nltk.tokenize import RegexpTokenizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

warnings.filterwarnings('ignore')
nltk.download('punkt')
nltk.download('stopwords')

# Set save path for model
SAVE_MODEL_PATH = os.path.join("models", "phishing.pkl")

def download_dataset():
    print("📥 Downloading phishing dataset from KaggleHub...")
    path = kagglehub.dataset_download("ashharfarooqui/phising-urls")
    dataset_path = os.path.join(path, "phishing_site_urls.csv")
    print(f"✅ Dataset downloaded at: {dataset_path}")
    return dataset_path

def load_data(csv_path):
    print("📊 Loading dataset...")
    df = pd.read_csv(csv_path)
    print(f"Dataset shape: {df.shape}")
    print(df.Label.value_counts())
    return df

def train_model(df):
    print("🚀 Training pipeline model...")

    pipeline = make_pipeline(
        CountVectorizer(tokenizer=RegexpTokenizer(r'[A-Za-z]+').tokenize, stop_words='english'),
        LogisticRegression(max_iter=1000)
    )

    X_train, X_test, y_train, y_test = train_test_split(
        df.URL, df.Label, test_size=0.25, random_state=42
    )

    pipeline.fit(X_train, y_train)

    train_acc = pipeline.score(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)

    print(f"✅ Training Accuracy: {train_acc:.4f}")
    print(f"✅ Testing Accuracy: {test_acc:.4f}")

    print("\n📋 Classification Report:")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    print("\n📊 Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Bad", "Good"], yticklabels=["Bad", "Good"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    return pipeline

def save_model(model):
    os.makedirs(os.path.dirname(SAVE_MODEL_PATH), exist_ok=True)
    with open(SAVE_MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"💾 Model saved to: {SAVE_MODEL_PATH}")

def main():
    dataset_path = download_dataset()
    df = load_data(dataset_path)
    model = train_model(df)
    save_model(model)
    print("\n✅ DONE: Model ready for Django integration!")

if __name__ == "__main__":
    main()
