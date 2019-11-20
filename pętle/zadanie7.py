

def przytnij(lista, start, stop):
    wynik = []
    czy_dodawać = False
    for el in lista:
        if not czy_dodawać and start(el):
            czy_dodawać = True
            wynik.append(el)
        if stop(el):
            break


    return wynik


def test_przytnij_zle_dane():
    rezult = przytnij([], 1, 3) # 1(1)

    assert rezult == []

def test_przytnij():

    rezult = przytnij(
        data = [1, 2, 3, 4, 1, 6, 7],
        start=lambda x: x ==2,
        stop = lambda x: x +1 >6
    )
    assert rezult == [2, 3, 4, 1, 6]

    rezult = przytnij (
        [8, 9, 3, 1 ,5 , 12, 19, 21, 0],
        start = lambda x:x % 3 == 0,
        stop=lambda x :x %4 ==0
    )
    assert rezult