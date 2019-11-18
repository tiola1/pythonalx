"""
lista =[-2, 10, 0, 5, 1, 16, 9]

wybierz_z_przedziału (lista, 5, 10)
[10, 5, 9]

"""

def wybierz_z_przedziału(lista, a, b):
    wynik = []
    for i in lista:
        #if i>= a and i <=b:
        # wynik.append(i)
        if i >= a and i <=b:
            wynik.append(i)
    return wynik



    return []


def test_wybierz_z_przedziału_pusta_lista():
    assert wybierz_z_przedziału([], 10, 20) == []

def test_wybierz_z_przedziału ():
    assert wybierz_z_przedziału([1, 10, 20, 30], 10, 20) == [10, 11, 20]
    assert wybierz_z_przedziału([1, 10, 20, 30], 10, 20) == [10, 11, 20]













lista = []

def wybierz_z_przedziału(lista, 5, 10):
    return True


def test_wybierz_z_przedziału_dla_listy():
    lista = []
    assert wybierz_z_przedziału (lista, 1, 100) == []
