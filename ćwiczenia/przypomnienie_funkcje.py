def do_potęgi(podstawa, wykładnik):
    return podstawa ** wykładnik   #return konczy funkcję

#uzycie:

wynik =  do_potęgi(2, 12)
wynik2 = do_potęgi(5, 5)


def unique_letters(text):
    u_letters = set(text)
    u_letters - "".join(u_letters)
    return u_letters, len(text)

dane = unique_letters("Ola_lalal")
print(dane)
print(type(dane))