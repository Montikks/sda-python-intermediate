import pickle

class MojeTrida:
    def __init__(self, jmeno, hodnota):
        self.jmeno = jmeno
        self.hodnota = hodnota


instance = MojeTrida('Priklad', 123)


with open('moje_trida.pkl', 'wb') as f:
    pickle.dump(instance, f)


with open('moje_trida.pkl', 'rb') as f:
    nactena_instance = pickle.load(f)

print(f'Jméno: {nactena_instance.jmeno}, Hodnota: {nactena_instance.hodnota}')
