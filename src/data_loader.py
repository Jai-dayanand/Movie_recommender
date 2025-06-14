import pandas as pd

class DataLoader:
    def __init__(self, movies_path='data/tmdb_5000_movies.csv', credits_path='data/tmdb_5000_credits.csv'):
        self.movies_path = movies_path
        self.credits_path = credits_path

    def load_data(self):
        movies = pd.read_csv(self.movies_path)
        credits = pd.read_csv(self.credits_path)

        # Rename movie_id to id for merging
        credits.rename(columns={'movie_id': 'id'}, inplace=True)

        # Merge both datasets
        movies = movies.merge(credits, on='id')

        # Rename 'title_x' to 'title' to avoid KeyError
        movies.rename(columns={'title_x': 'title'}, inplace=True)

        # Drop unnecessary columns (note we use 'title' now)
        movies = movies[['id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        movies.dropna(inplace=True)

        return movies
