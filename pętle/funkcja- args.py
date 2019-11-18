"""
Funkcja z dowolną liczbą parametrów
"""
#funkcja mnoży wartosci podane do jej środka
#możliwe podanie nieznanej liczby parametrów

def iloczyn(start,*args):
    wynik = start
    for nr, arg in enumerate(args,100):
        #print(f"Pozycja {nr} = {arg}")
        wynik *= arg
    return wynik

print(iloczyn(2,1,2,3,4,5))