from dataclasses import dataclass
import pickle


@dataclass
class Point:
    x: int = 0
    y: int = 0


if __name__ == '__main__':
    point = Point(4, 2)
    with open('point.pkl', 'wb') as f:
        pickle.dump(point, f)

# Pickle je dobry aj napriklad na pause a resume pri dlhsich vypoctoch.
# Vieme si ulozit medzivypocty do suboru a nasledne vo vypocte pokracovat.
