# Movie Recommendation System

A Python-based movie recommendation system that suggests similar movies based on genre features and average ratings. This project uses **TF-IDF** vectorization and the **k-nearest neighbors (k-NN)** algorithm for similarity computation.

## Features

- Computes recommendations for a given movie title.
- Uses cosine similarity to find similar movies.
- Sorts recommendations by average user ratings.

---

Data Requirements
This project requires two CSV files:

1. **movies.csv**: Contains movie metadata with the following columns:
   - `movieId`: Unique identifier for each movie.
   - `title`: The name of the movie.
   - `genres`: Genres associated with the movie, separated by `|`.

2. **ratings.csv**: Contains user ratings with the following columns:
   - `userId`: ID of the user.
   - `movieId`: ID of the movie.
   - `rating`: Rating given by the user (float).
.


## Usage

Prepare your data: Place the movies.csv and ratings.csv files in the project directory.
Run the script and then Input the title of a movie (with the year in parentheses) when prompted:

***Example Input***

Enter the movie name (with year of release): The Matrix (1999)
