# zapytaj uzytkownika o 10 liczb i wypisz ich srednie
# skorzystaj z pętli for oraz funkcji range
suma = 0
for i in range(10):
    x = input("Podaj liczbę")
    x = int(x)
    suma = suma + x

print(suma/10)


if suma/10 > 5:
    print("da dam")


