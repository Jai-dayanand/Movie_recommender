import streamlit as st
from src.data_loader import DataLoader
from src.recommender import Recommender

# Load data
data_loader = DataLoader('data/tmdb_5000_movies.csv')
movies = data_loader.load_data()
recommender = Recommender(movies)

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎥", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF6F61;'>🎬 Movie Recommender Lite</h1>", unsafe_allow_html=True)
st.write("---")

# Movie selection
col1, col2 = st.columns(2)

with col1:
    movie_list = movies['title'].sort_values().unique()
    selected_movie = st.selectbox("Select a movie:", movie_list)

with col2:
    all_genres = sorted(set(" ".join(movies['genres']).split()))
    genre_filter = st.multiselect("Optional: Filter recommendations by genre", all_genres)

# Recommendation button
if st.button("Get Recommendations 🎯", use_container_width=True):
    recommendations = recommender.recommend(selected_movie)

    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.subheader("🎯 Recommended Movies:")
        count = 0
        for movie_title in recommendations:
            # Apply genre filter
            movie_row = movies[movies['title'] == movie_title]
            if genre_filter:
                movie_genres = movie_row.iloc[0]['genres'].split()
                if not any(g in movie_genres for g in genre_filter):
                    continue
            count += 1
            st.write(f"**{count}. {movie_title}**")

        if count == 0:
            st.warning("No recommendations match the selected genre filter.")

# Add full dataset viewer (optional)
with st.expander("🔎 Browse Full Dataset"):
    st.dataframe(movies[['title', 'genres', 'overview']])
