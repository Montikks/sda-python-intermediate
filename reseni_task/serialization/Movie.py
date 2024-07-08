import csv
from dataclasses import dataclass
from typing import List

@dataclass
class Movie:
    movie_id: int
    title: str
    genre: str
    rating: float
    year: int

def read_movies_csv(file_name: str) -> List[Movie]:
    movies = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie_id = int(row['MovieID'])
            title = row['Title']
            genre = row['Genre']
            rating = float(row['Rating'])
            year = int(row['Year'])
            movie = Movie(movie_id, title, genre, rating, year)
            movies.append(movie)
    return movies

def sort_movies_by(movies: List[Movie], attribute: str, reverse: bool = False) -> List[Movie]:
    if attribute not in ['movie_id', 'title', 'genre', 'rating', 'year']:
        raise ValueError(f"Neplatný atribut '{attribute}' pro řazení.")

    sorted_movies = sorted(movies, key=lambda x: getattr(x, attribute), reverse=reverse)

    return sorted_movies

if __name__ == "__main__":
    movies = read_movies_csv('movies.csv')

    sorted_movies_by_title = sort_movies_by(movies, 'title')
    for movie in sorted_movies_by_title:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")

    print()

    sorted_movies_by_rating = sort_movies_by(movies, 'rating', reverse=True)
    for movie in sorted_movies_by_rating:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")
