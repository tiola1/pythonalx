"""
Przekazywanie listy parametrów nazwanych
"""
def fun_parametry(nr,**kwargs):
    print ("nr pracownika=",nr)
    print(kwargs ["imie"])

fun_parametry(102, imie="Jan", nazwisko="Kowalski",
              email="jk@firma.pl", wiek="44")


