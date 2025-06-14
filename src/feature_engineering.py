import ast

class FeatureEngineering:
    def __init__(self, movies):
        self.movies = movies

    def parse(self, obj):
        try:
            L = []
            for i in ast.literal_eval(obj):
                L.append(i['name'])
            return L
        except:
            return []

    def get_director(self, obj):
        try:
            for i in ast.literal_eval(obj):
                if i['job'] == 'Director':
                    return i['name']
            return ''
        except:
            return ''

    def preprocess(self):
        self.movies['genres'] = self.movies['genres'].apply(self.parse)
        self.movies['keywords'] = self.movies['keywords'].apply(self.parse)
        self.movies['cast'] = self.movies['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)][:3])
        self.movies['crew'] = self.movies['crew'].apply(self.get_director)

        self.movies['tags'] = self.movies['overview'] + ' ' + \
                               self.movies['genres'].apply(lambda x: ' '.join(x)) + ' ' + \
                               self.movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' + \
                               self.movies['cast'].apply(lambda x: ' '.join(x)) + ' ' + \
                               self.movies['crew']

        self.movies['tags'] = self.movies['tags'].str.lower()

        return self.movies[['id', 'title', 'tags']]
