
#zad 1 - typy danych
# str
# int
# float
# complex
# bool

#ctrl + /

#zad 2 - struktury danych
# tuple
# list
# dict
# set

#zad 3 wymien sposoby na posortowanie listy

lista = [3,1,2]
lista.sort() # a nie lista.sorted()
sorted(lista)

#zad 4

slownik = {}
slownik ['ala'] # dostanę wyjątwk bo nie ma takiego klucza

try:
    slownik['ala']
except KeyError:
    print("Brak takiego klucza")

if 'ala' in slownik: #slownik.keys()
    print(slownik['ala'])

slownik.get('ala') # domyślnie zwracana jest wartość None jesli klucza nie ma
slownik.get('ala', "brak") #brak jest domyślną wartością

#zadanie 5 zdefiniuj funkję która przyjmie dwa napisy, zlaczy je i zwroci ten polaczony napis, ale odwrocony

def zlacz_teksty(a,b):
    c = a + b
    return c[::-1]