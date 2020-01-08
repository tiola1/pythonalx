
import json

#srializacja zmiennych do formatu json

pracownik = {
    "imie":"Jan",
    "nazwisko":"Kowalski",
    "wiek":42,
    "dostępy":['SALA01', 'SALA02', 'SALA03'],
    "wynagrodzenie":12345.67,
    "manager":False,
    "auto":None
}

#zapis (serializacja) do pliku wartości zmiennej
with open ("pracownik.dat","wt")as fd :
    json.dump(pracownik,fd)
