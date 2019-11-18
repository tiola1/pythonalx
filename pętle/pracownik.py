"""
Tworzenie rekordu pracownika
2 parametry obowiązkowe, 2 opcjonalne,
ma zwrócić zmienną typu słownik
"""

def utwórz_pracownika(imię, nazwisko, email="info@firma.pl", telefon =None):
    pracownik = dict()
    pracownik ["imię"] = imię
    pracownik ["nazwisko"] = nazwisko
    pracownik ["email"] = email
    pracownik ["telefon"] = telefon
    return pracownik

print(utwórz_pracownika("Jan", "Kowalski"))
print(utwórz_pracownika("Adam", "Nowak", "annanowak@firma.pl", "501890778"))
print(utwórz_pracownika("Jan", "Zieliński", telefon= "601602603"))
print(utwórz_pracownika("Jan", "Zieliński", "jzielinski@firma.pl"))
print(utwórz_pracownika("Jan", "Zieliński", telefon= "601602603", email="jz@firma.pl"))

