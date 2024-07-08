import csv
from dataclasses import dataclass

# Task 1
# Napis funkciu read_movies_csv(file_name), ktora nacita zo suboru data o filmoch
# a nacita ich do dataclassy Movie.
# movies.csv ma format
# MovieID,Title,Genre,Rating,Year
# Teda napriklad:
"""
1,The Shawshank Redemption,Drama,9.3,1994
2,The Godfather,Crime,9.2,1972
3,The Dark Knight,Action,9.0,2008
4,Pulp Fiction,Crime,8.9,1994
5,Forrest Gump,Drama,8.8,1994
6,Inception,Sci-Fi,8.8,2010
"""


@dataclass(frozen=True)
class Movie:
    id: int
    title: str
    genre: str
    rating: float
    release_year: int


def read_movies_csv(file_name):
    with open(file_name) as in_file:
        reader = csv.reader(in_file)
        loaded_movies = []
        for row in reader:
            id_, title, genre, rating, year = row
            loaded_movies.append(
                Movie(
                    int(id_),
                    title,
                    genre,
                    float(rating),
                    int(year),
                )
            )

    return loaded_movies

# Task 2
# Napis funkciu filter_movies(movies, genre), ktora dostane list filmov a vrati iba
# filmy zanru dodaneho v druhom parametri `genre`


def filter_movies(movies, genre):
    return [movie for movie in movies if movie.genre == genre]

# Task 3
# Napis funkciu sort_movies_by(movies, attribute, reverse=False), ktora vrati
# potriedeny list filmov podla atributu zadaneho ako string cez parameter `attribute`.


def sort_movies_by(movies, attribute, reverse=False):
    def movie_key(movie):
        return getattr(movie, attribute)

    return sorted(movies, key=movie_key, reverse=reverse)


if __name__ == "__main__":
    movies = read_movies_csv('movies.csv')
    print(filter_movies(movies, 'Crime'))
    print(filter_movies(movies, 'IDontExist'))

    print(sort_movies_by(movies, 'id'))
    print(sort_movies_by(movies, 'title'))
    print(sort_movies_by(movies, 'release_year', reverse=True))
