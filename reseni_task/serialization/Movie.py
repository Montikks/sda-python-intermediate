from dataclasses import dataclass
from typing import List


@dataclass
class Movie:
    movie_id: int
    title: str
    genre: str
    rating: float
    year: int



def filter_movies(movies: List[Movie], genre: str) -> List[Movie]:

    filtered_movies = []


    for movie in movies:
        if movie.genre == genre:
            filtered_movies.append(movie)


    return filtered_movies



def get_unique_genres(movies: List[Movie]) -> List[str]:
    genres = set()
    for movie in movies:
        genres.add(movie.genre)
    return list(genres)



if __name__ == "__main__":

    movies = [
        Movie(1, "The Shawshank Redemption", "Drama", 9.3, 1994),
        Movie(2, "The Godfather", "Crime", 9.2, 1972),
        Movie(3, "The Dark Knight", "Action", 9.0, 2008),
        Movie(4, "Pulp Fiction", "Crime", 8.9, 1994),
        Movie(5, "Forrest Gump", "Drama", 8.8, 1994),
        Movie(6, "Inception", "Sci-Fi", 8.8, 2010)
    ]


    genres = get_unique_genres(movies)


    print("Dostupné žánry:")
    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")


    selected_genre_index = int(input("Zadej číslo žánru, který chceš zobrazit: "))


    if selected_genre_index < 1 or selected_genre_index > len(genres):
        print("Neplatná volba žánru.")
    else:
        selected_genre = genres[selected_genre_index - 1]
        filtered_movies = filter_movies(movies, selected_genre)

        # Vypis filtrovanych filmu
        print(f"\nFilmy žánru '{selected_genre}':")
        for movie in filtered_movies:
            print(f"{movie.title} ({movie.year}), Hodnocení: {movie.rating}")
