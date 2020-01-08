
#definicja klasy
class Pies:

    gatunek = "Canis Familiaris"
    ile = 0


    def __init__(self,imie,waga):
        self.imie = imie
        self.waga = waga
        Pies.ile += 1

    def szczekaj(self):
        print(f"{self.imie} szczeka")

    @classmethod
    def incr(cls):



#tworzę instancję klasy Pies
#jest przypisana do zmiennej azor

azor = Pies ("Azor", "10")
print
reks = Pies("Reks", "85")

reks.szczekaj()
Pies.szczekaj(azor)
azor.szczekaj()

# print(azor)  #obiekt typu pies (obiekt tej klasy)
#
# print(isinstance(azor, Pies))
# print((isinstance(azor, object)))
#
# print(azor.waga)
# print(dir(azor))
#
# azor.waga =10
# azor.waga +=1
# print(azor.waga)
#
# print(azor == reks)
# print(azor, reks)
#
# azor = Pies ("Azor, 10")
# reks = Pies("Reks", "10")