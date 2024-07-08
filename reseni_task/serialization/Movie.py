from dataclasses import dataclass
from typing import List


@dataclass
class Movie:
    movie_id: int
    title: str
    genre: str
    rating: float
    year: int


def sort_movies_by(movies: List[Movie], attribute: str, reverse: bool = False) -> List[Movie]:

    if attribute not in ['movie_id', 'title', 'genre', 'rating', 'year']:
        raise ValueError(f"Neplatný atribut '{attribute}' pro řazení.")


    def get_attribute_value(movie):
        return getattr(movie, attribute)


    sorted_movies = sorted(movies, key=get_attribute_value, reverse=reverse)

    return sorted_movies



if __name__ == "__main__":

    movies = [
        Movie(1, "The Shawshank Redemption", "Drama", 9.3, 1994),
        Movie(2, "The Godfather", "Crime", 9.2, 1972),
        Movie(3, "The Dark Knight", "Action", 9.0, 2008),
        Movie(4, "Pulp Fiction", "Crime", 8.9, 1994),
        Movie(5, "Forrest Gump", "Drama", 8.8, 1994),
        Movie(6, "Inception", "Sci-Fi", 8.8, 2010)
    ]


    sorted_movies_by_title = sort_movies_by(movies, 'title')
    print("Filmy seřazené podle názvu vzestupně:")
    for movie in sorted_movies_by_title:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")

    print()


    sorted_movies_by_rating = sort_movies_by(movies, 'rating', reverse=True)
    print("Filmy seřazené podle hodnocení sestupně:")
    for movie in sorted_movies_by_rating:
        print(f"{movie.title} ({movie.year}) - Hodnocení: {movie.rating}")
