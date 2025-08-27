import os
import pickle
from django.conf import settings

def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'models', 'phishing.pkl')
    try:
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {str(e)}")