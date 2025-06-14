import streamlit as st
from src.data_loader import DataLoader
from src.recommender import Recommender

# Load data
data_loader = DataLoader('data/tmdb_5000_movies.csv')
movies = data_loader.load_data()
recommender = Recommender(movies)

st.title("🎬 Movie Recommender System")

movie_list = movies['title'].sort_values().unique()
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button("Recommend"):
    recommendations = recommender.recommend(selected_movie)
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.subheader("Top Recommendations:")
        for movie in recommendations:
            st.write(movie)

# BONUS: explore genres
if st.checkbox("Browse by Genre"):
    genre = st.selectbox("Select genre:", sorted(set(" ".join(movies['genres']).split())))
    filtered = movies[movies['genres'].str.contains(genre)]
    st.write(filtered[['title', 'genres']])
