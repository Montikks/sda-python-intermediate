import pickle
from pickle_from import Point


with open('point.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
