napis = "Ala ma kota"

for znak in napis:
    znak = znak.upper()
    print(znak)

print("Wartość w znak po skonczeniu pętli ", znak)



elementy = (1, 'a', 2, 'c')

for e in elementy:
    print(e)


lista = [4, 12, 11, 1]
slownik = {1:"a", "Ala": "kot", "Albert": "Eistein"}

zbiór = {1, 2, 3, 'a'}
for el in zbiór:
    print(el)

zbior = {40, 181, 100,}

liczby = [1, 2, 3, 6, 7, 20, 30]
for liczba in liczby:
    if liczba == 0:
        break
       # continue
       # break #wychodzenie z pętli
    print(10/liczba)
else:
    print("wykonałem się")
print("jestem po pętli")

print(range(10))
print(list(range(10)))
print(set(range(10)))

for i in range(10):
    print(i)


