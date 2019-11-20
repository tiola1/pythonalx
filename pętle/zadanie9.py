"""
a)Napisz funkcję, która wymnozy przez siebie elementy
podane w liscie wejsciowej

pomnoz(lista)

b)pomnoz (1,2)

pomnoz(4,5,1)
20

c) napisz funkcję, która wybierze i zwróci z podanego napisu liste liczb

x = "a1b2c1d2"
[1,2,1,2]
x = "a100v200"
[1, 0, 0, 2, 0, 0]

d)
x = "a100v200"
[100,200]

"""



def wybierz_cyfry(napis):
    wynik = []
    for litera in napis:
        if litera.isdigit():
            wynik.append(litera)
    return wynik

x = "a1b2c1d2"
print(wybierz_cyfry(x))

