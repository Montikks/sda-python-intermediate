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
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            movie_id = int(row[0])
            title = row[1]
            genre = row[2]
            rating = float(row[3])
            year = int(row[4])
            movie = Movie(movie_id, title, genre, rating, year)
            movies.append(movie)
    return movies

def sort_movies_by(movies: List[Movie], attribute: str, reverse: bool = False) -> List[Movie]:
    if attribute not in ['movie_id', 'title', 'genre', 'rating', 'year']:
        raise ValueError(f"Neplatný atribut '{attribute}' pro řazení.")

    def get_attribute_value(movie):
        return getattr(movie, attribute)

    sorted_movies = sorted(movies, key=get_attribute_value, reverse=reverse)

    return sorted_movies

if __name__ == "__main__":

    movies = read_movies_csv('movies.csv')


    sorted_movies_by_title = sort_movies_by(movies, 'title')
    print("Filmy seřazené podle názvu vzestupně:")
    for movie in sorted_movies_by_title:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")

    print()


    sorted_movies_by_rating = sort_movies_by(movies, 'rating', reverse=True)
    print("Filmy seřazené podle hodnocení sestupně:")
    for movie in sorted_movies_by_rating:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")
