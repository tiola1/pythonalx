import pickle

#print(dir(pickle))
#print(help(pickle.dumps))

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

os = Osoba("Ania", 25)
os2 = Osoba("Bolek", 65)

with open("osoby.pickle", 'wb') as f:
    pickle.dumps(os.f)