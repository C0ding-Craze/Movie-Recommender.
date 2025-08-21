# 🎬 Movie Recommendation System  

A Python-based **content-based movie recommendation system** that suggests similar movies based on **genres** and **average ratings**.  
This project leverages **TF-IDF Vectorization** and the **k-Nearest Neighbors (k-NN)** algorithm with cosine similarity for accurate recommendations.  

---

## Features  

- Computes recommendations for a given movie title  
- Uses **cosine similarity** on movie genres to find similar titles  
- Sorts recommended movies by **average user ratings**  
- Simple **command-line interface**  

---

## Dataset Requirements  

This project requires two CSV files from the [MovieLens dataset](https://grouplens.org/datasets/movielens/):  

1. **movies.csv**  
   - `movieId`: Unique identifier for each movie  
   - `title`: The name of the movie (with year of release)  
   - `genres`: Genres associated with the movie, separated by `|`  

2. **ratings.csv**  
   - `userId`: Unique identifier of the user  
   - `movieId`: ID of the movie  
   - `rating`: Rating given by the user (float)  

---  

**Example Input**  

Enter the movie name (with year of release): Toy Story (1995)

**Example Output**

                                         title  rating
                        Shrek the Third (2007)     3.0
                Tale of Despereaux, The (2008)     3.0
                      The Good Dinosaur (2015)     3.0
                                  Turbo (2013)     2.5

## Package Requirements  

To run this project, you need the following Python libraries:  

- **pandas**  
- **scikit-learn**  

You can install them using:  

```bash
pip install pandas scikit-learn
