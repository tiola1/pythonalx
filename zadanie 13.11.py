"""
Napisz funkcję która sprawdzi czy dany tekst jest palindronem

tzn. czy jest taki sam czytany wstecz

is_palindrom ("kajak") is True
is_palindrom ("kot") is False

1. napisać test

2. funkcję, która ten test zda
"""

# pisanie testu

def ia_palindrom(tekst):
    return True

#def is_palindrom(napis):
    #if napis == napis [::-1]:
        #return True
    #print(a)
    #pass

#def is_palindrom(kajak):
    #if kajak == kajak [::-1]:
     #   return True
     # return False


#zeby zdac drugi assert
def is_palindrom(tekst):

   # tekst = tekst.lower().replace(" ","").replace(".","").replace((",", "") można byloby to zrobic bardziej estetycznie
    signs_to_remove = " .,:!?"
   for s in signs_to_remove:
       tekst = tekst.replace(s, "")






def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("A to idiota.") is True
    assert is_palindrom("Ada, gmina za nim gada.") is True   # dopisać rozwiązania testu

def test_is_palindrom_for_palindrom():
    assert is_palindrom("ala ma kota") is False
    


