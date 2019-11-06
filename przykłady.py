#definicja funkcji, prodecury, zestawu
def nazwa_funkcji(): # ta funkcja nie przyjmuje żadnych argumentów
    #to jest ciało funkcji
    #blok instrukcji
    print ("Hello World")


nazwa_funkcji()

def funkcja_z_argumentem(x):
    """
    x - argument mojej funkcji. Mogę używać go wewnątrz niej
    będzie dostępny pod nazwą x
    """
    #return None - to jest domyślne zachowanie

def do_piątej(liczba):
    print(liczba**5)

x = do_piątej(4)
print(x)


#funkcja która zwróci kopie napisu tylko z dużymi literami

def powiększ(napis):
    return napis.upper







