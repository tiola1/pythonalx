"""
Napisać funkcję do obliczenia pola i obwodu kola

"""
from math import pi, sin


def oblicz_pole_koła(r):
    return pi*r**2

def oblicz_obwód_koła(r):
    return 2*pi*r

def oblicz_pole_i_obwód_koła(r):
    return oblicz_pole_koła(r), oblicz_obwód_koła(r)

print(oblicz_pole_i_obwód_koła(4))
