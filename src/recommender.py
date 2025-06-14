from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, movies):
        self.movies = movies
        self.vectorizer = CountVectorizer(max_features=5000, stop_words='english')
        self.vectors = self.vectorizer.fit_transform(movies['tags']).toarray()
        self.similarity = cosine_similarity(self.vectors)

    def recommend(self, movie_name):
        try:
            index = self.movies[self.movies['title'].str.lower() == movie_name.lower()].index[0]
        except IndexError:
            return f"Movie '{movie_name}' not found in database."

        distances = sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_titles = [self.movies.iloc[i[0]].title for i in distances[1:6]]
        return recommended_titles
