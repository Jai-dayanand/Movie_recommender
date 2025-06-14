import pandas as pd
import ast

class DataLoader:
    def __init__(self, movie_path):
        self.movie_path = movie_path

    def load_data(self):
        movies = pd.read_csv(self.movie_path)

        # Parse genres and keywords columns
        movies['genres'] = movies['genres'].apply(self.extract_names)
        movies['keywords'] = movies['keywords'].apply(self.extract_names)

        # Create 'tags' column combining genres + keywords + overview
        movies['overview'] = movies['overview'].fillna('')
        movies['tags'] = movies['overview'] + ' ' + movies['genres'] + ' ' + movies['keywords']

        movies = movies[['id', 'title', 'overview', 'genres', 'keywords', 'tags']]

        return movies

    def extract_names(self, obj):
        try:
            L = []
            for item in ast.literal_eval(obj):
                L.append(item['name'])
            return " ".join(L)
        except:
            return ""
