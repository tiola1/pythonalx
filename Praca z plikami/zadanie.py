"""
1)Napisz funkcję, która otworzy podany jako argument plik (podana nazwa pliku lub ścieżka)
i wypisze go numerując linie


#plik.txt
raz
dwa
trzy


wynik:
1 raz
2 dwa
3 trzy


2) Pozwól na uruchomienie programu z command line:

$ python numerator.py test
"""


def ponumeruj (nazwa_pliku):
    with open(nazwa_pliku) as f:
        i = 1
        for line in f:
            print((line.rstrip()))
            i += 1
ponumeruj('tworzenie_i_zapisywanie.py')