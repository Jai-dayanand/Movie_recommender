# 🎬 Movie Recommender System

A Content-Based Movie Recommender System using NLP, vectorization, and cosine similarity — with a clean Streamlit UI.

---

## 💂 Project Structure

Movie\_recommender/
│
├── data/
│   ├── tmdb\_5000\_movies.csv
│   └── tmdb\_5000\_credits.csv
│
├── src/
│   ├── data\_loader.py
│   └── recommender.py
│
├── app\_streamlit.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 🚀 Features

* Content-based recommendation
* Search by movie title
* Filter by genre
* Simple, clean Streamlit UI

---

## 💻 Setup

```bash
git clone https://github.com/yourusername/movie-recommender
cd Movie_recommender
python -m venv venv
venv\Scripts\activate    # (Windows) OR source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
```

Download datasets:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Place them inside `/data` folder.

Finally run:

```bash
streamlit run app_streamlit.py
```

Visit: `http://localhost:8501`

---

## 📊 Dataset:

TMDB 5000 Movie Dataset (Kaggle)

## 👨‍💼 Author:

Jai Dayanand

---
