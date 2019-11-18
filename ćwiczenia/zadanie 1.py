import unittest


"""
Napisz funkcję, która sprawdzi, czy podana liczba jest liczbą pierwszą

"""

def czy_pierwsza(x):
    """Ten obszar nazywa się docstring i służy
    do tworzenia dokumentacji funkcji
    Sprawdza czy x jest liczbą pierwszą
    Przykłady użycia:
    #przykłady uzycia doctestów
    >>>czy_pierwsza(10)
    True
    >>>czy_pierwsza(10)
    False"""

    for liczba in range (2, x):
        if x % liczba == 0
            return False
        return True




#print(help(czy_pierwsza))
#prymitywna forma testów -bez zadnego freamworka


assert czy_pierwsza(2) is True
assert czy_pierwsza(7) is True
assert czy_pierwsza(10) is False

class TestCzyPierwsza(unittest.TestCase):

    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_pierwsza(7), True)

    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_pierwsza(11), True)



    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertIs(czy_pierwsza((10), False)
        self.assertIs(czy_pierwsza((10), False)
