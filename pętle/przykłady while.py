#losowanie

import random # "wkleja kod napisany przez kogos w to miejsce"

print(dir(random))
print(help(random.randint))
print(random.randint(1, 10))

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("Polozenie gracza", gracz_x, gracz_y)
print("Polozenie skarbu", skarb_x, skarb_y)

print(help(abs))

print(abs(100))   #wartosc bezwzględna
print(abs(-100))

odelglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

x = 1
warunek = x > 7
while x > 7:
    print ("jestem w pętli")

while False:
    print("Jestem w pętli")

while True:
    print("Jestem w pętli")
    break

x = 10
while x > 0:
    if x == 6:
        x -= 1
        continue
    print(x)
    x = x -1

while True:
    instrukcja = input("by zakonczyc wciśnij: k")
    if instrukcja == 'k':
        break

