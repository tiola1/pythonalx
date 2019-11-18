"""
Zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu.
lata_przestępne(1990, 2020)
[1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

rok przestępny jest co 4 lata, o ile nie dzieli się przez 100
albo dzieli sie przez 400
Do sprawdzenia (!!)

Punkt startu 0,


def test_lata_przestępne():
    assert lata_przestępne(2020, 2030) == [2020, 2024, 2028]
"""

def czy_przestępny(rok):
 #   if rok%4==0 and (rok%100!= 0 or rok%400==0):
    #if (rok%4==0 and rok%100!=0) or (rok%4==0 and rok%400==0): # mozna tutaj dopisać True and False
    return (rok%4==0 and rok%100!=0) or (rok%4==0 and rok%400==0)


def lata_przestępne (rok_od, rok_do):
    if rok_od>rok_do: #walidacja zakresu lat
        return None

    lata = list()
    for rok in range (rok_od, rok_do+1):
        if czy_przestępny(rok):
            lata.append(rok)
    return lata

#print(lata_przestępne(2000, 2030))
def test_lata_przestępne():
  assert (lata_przestępne(2020, 2030) == [2020, 2024, 2028]) is True
