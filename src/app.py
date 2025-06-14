from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering
from src.recommender import MovieRecommender

def main():
    data_loader = DataLoader()
    movies = data_loader.load_data()

    fe = FeatureEngineering(movies)
    movies = fe.preprocess()

    recommender = MovieRecommender(movies)

    while True:
        movie_name = input("Enter a movie name (or type 'exit' to quit): ")
        if movie_name.lower() == 'exit':
            break

        recommendations = recommender.recommend(movie_name)
        print("\nRecommended Movies:")
        if isinstance(recommendations, str):
            print(recommendations)
        else:
            for movie in recommendations:
                print(movie)
        print("\n")

if __name__ == "__main__":
    main()
