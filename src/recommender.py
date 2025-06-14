from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class Recommender:
    def __init__(self, movies):
        self.movies = movies
        self.vectorizer = CountVectorizer(max_features=5000, stop_words='english')
        self.vectors = self.vectorizer.fit_transform(self.movies['tags']).toarray()
        self.similarity = cosine_similarity(self.vectors)

    def recommend(self, movie):
        movie = movie.lower()
        if movie not in self.movies['title'].str.lower().values:
            return f"Movie '{movie}' not found."

        idx = self.movies[self.movies['title'].str.lower() == movie].index[0]
        distances = sorted(list(enumerate(self.similarity[idx])), reverse=True, key=lambda x: x[1])
        recommendations = []
        for i in distances[1:6]:
            recommendations.append(self.movies.iloc[i[0]].title)
        return recommendations
