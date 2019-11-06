import random

DEBUG = True

#Teraz wylosujemy początkowe położenia

gracz_x = random.randint(1,10)
gracz_y = random.randint (1,10)
skarb_x = random.randint (1,10)
skarb_y = random. randint (1,10)

# Obliczam odległość po wylosowaniu

print("Położenie gracza", gracz_x, gracz_y)
print("Położenie skarbu", skarb_x, skarb_y)

# Obliczam odległość po wylosowaniu
odległość_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)


# w zależności od wartości zmiennej DEBUG
#printuje informacje o położeniu skarbu i gracza


if DEBUG:
    print(f"Położenie gracza (x={gracz_x}, y={gracz_y})")
    print(f"Położenie skarbu (x={skarb_x}, y={skarb_y})")
    print(f"Minimalna liczba ruchów = {odległość_po_wylosowaniu }")


print(""""
Witaj!

Twoim zadaniem jest odnalezienie skarbu!
Możesz się poruszać wpisując komendy:
w - góra
s - dół
a - lewo
d- prawo

Uważaj! Możesz wypaść poza planszę.
Po każdym ruchu możesz dostać informację o tym czy się zblizasz czy oddalsz

Zaczynamy!
""")

while True:

    # pytamy gracza o ruch
    ruch = input("Wpisz komendę (a- lewo, d-prawo, w-góra, s-dół)")

    odleglość_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    #zmieniamy pozycję gracza zgodnie z komendą

    if ruch == 'a':
        gracz_x = gracz_x - 1
    elif ruch == 's':
        gracz_y = gracz_y - 1
    elif ruch == 'd':
        gracz_x += 1
    elif ruch == 'w':
        gracz_y += 1
    else:
        print("Trzymaj sie reguł... $#^&*%%!!")

    if DEBUG:
        print(f"Położenie gracza po ruchu (x={gracz_x}, y={gracz_y})")
        print(f"Położenie skarbu  (x={skarb_x}, y={skarb_y})")
    # po ruchu robimy sprawdzenia
    if not (1 <= gracz_x <= 10 and 1 <= gracz_y <= 10):
        print("Wypadłeś poza planszę")
    break

    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if DEBUG:
        print(f"Odl przed:{odleglość_przed}")
        print(f"Odl po:{odleglosc_po_ruchu}")



    if odleglosc_po_ruchu < odleglość_przed :
        print("cieplo")
    elif odleglosc_po_ruchu > odległość_po_wylosowaniu:
        print("zimno")
    else:
        print("bez zmian")

