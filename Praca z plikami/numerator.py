import sys

try:
nazwa_pliku =sys.argv[1]

except IndexError:
    print("Nie podano nazwy pliku")
    exit()

def ponumeruj(nazwa_pliku):

    with open(nazwa_pliku) as f:
        i = 1
        for line in f:
            print(i, ". ", line.rstrip())
            i += 1


try :
 ponumeruj(nazwa_pliku)
except FileNotFoundError:
    print("Nie ma takiego pliku")