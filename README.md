````markdown
# Phishing Link Detection Using ML and Crowdsourcing

This project implements a hybrid phishing detection system using **Logistic Regression** and a **crowdsourcing feedback loop**. It provides a web-based interface (built with Django) where users can submit URLs to check if they are safe or suspicious. The backend continuously learns from user feedback and adapts to new phishing patterns.

---

## 🚀 Features
- Machine Learning model (Logistic Regression chosen as best performer).
- Web interface built with Django.
- SQLite database for storing URLs, predictions, and user feedback.
- Crowdsourcing mechanism for reporting false positives/negatives.
- Real-time phishing link detection.

---

## 🛠️ Installation and Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bibeksuhang/Phising-link-detetction-using-ML-and-Crowdsourcing.git
cd Phising-link-detetction-using-ML-and-Crowdsourcing
````

### 2️⃣ Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Since there is no `requirements.txt`, install the core dependencies manually:

```bash
pip install django scikit-learn pandas numpy matplotlib
```

If you encounter missing packages later, install them as prompted.

### 4️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional for Admin Access)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Now, open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

* `phishing/` → Django project folder.
* `ml_model/` → Contains ML training and prediction scripts.
* `templates/` → Frontend HTML templates.
* `db.sqlite3` → SQLite database.
* `manage.py` → Django project manager.

---

## ⚡ Usage

1. Enter a URL in the web form.
2. The system classifies it as **Safe** or **Phishing**.
3. Users can provide feedback to improve detection accuracy.
4. The model updates dynamically based on crowdsourced data.

---

## ✅ Requirements

* Python 3.8+
* Django 5.x
* scikit-learn
* pandas
* numpy
* matplotlib

---
Expected Results 
<img width="739" height="586" alt="Screenshot 2025-07-25 125207" src="https://github.com/user-attachments/assets/971b2d79-065d-4380-85a7-583dbde65ca3" />


## 📜 License

This project is for academic purposes (MSc Information Technology project).
Use responsibly.
```
