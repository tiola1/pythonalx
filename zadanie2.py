"""
Napisz funkcję zwracającą zbiór wszytskich znaków występujących w zadanym napisie
więcej niż podana liczba razy
np:

#>>>więcej_niż("ala ma kota a kot ma ale", 3)
{'a', ' '}
"""
def więcej_niż(text: str,  b):
    result = set()
    for s in set(text):
        if text.count(s) > b:
            result.add(s)
    return result

def test_więcej_niż_dla_pustego_napisu():
    assert więcej_niż ("", 0) == set() #nie {}

def test_więcej_niż_dla_niepustego_napisu():
    assert więcej_niż("aaa bbb cc dd", 2) == {"a", "b", " "}