# First install pandas and scikit-learn.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

movies_df = pd.read_csv("movies.csv")
ratings_df = pd.read_csv("ratings.csv")

average_rating = ratings_df.groupby("movieId")["rating"].mean().reset_index()

movies = pd.merge(movies_df, average_rating, on="movieId")
movies["combined_features"] = movies["genres"]

tfidf_vectorizer = TfidfVectorizer()
feature_matrix = tfidf_vectorizer.fit_transform(movies["combined_features"])

knn_model = NearestNeighbors(metric="cosine", algorithm="brute")
knn_model.fit(feature_matrix)

def recommend_movies(title, movies_df=movies, model=knn_model, n_recommendations=5):

    if title not in movies_df["title"].values:
        return "\nMovie not found in the database.\n"
    
    index = movies_df.index[movies_df["title"] == title].to_list()[0]

    distances, indices = model.kneighbors(feature_matrix[index], n_neighbors=n_recommendations+1)

    similar_indices = indices.flatten()[1:]

    similar_movies = movies_df.iloc[similar_indices]
    similar_movies = similar_movies.sort_values(by="rating", ascending=False)

    result = similar_movies[["title", "rating"]].to_string(index=False, float_format="%.1f")

    return result

if __name__=="__main__":

    movie_to_compare = input("\nEnter the movie name (with year of release): ")
    print(recommend_movies(f"{movie_to_compare}"))  