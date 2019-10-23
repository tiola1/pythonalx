#
#Typ danych napisy (albo string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
napis3 = 'A to jest "cudzysłów"'
napis4 = "A to jest \"cudzysłów\" "
napis5 = "Znaki specjalne: \t \n \r "

#długosc = len(napis1)
#print("Długosc zmiennej napis1 to ",długosc, "znaków")



#wiek = input("Podaj wiek:")
#print("Twój wiek to: ",wiek.strip())

s = "Ruda tańczy jak szalona"
print(s.capitalize()) #kapitalki
print(s.upper()) #w góre
print(s.lower()) # w dół
print(s.title()) # formatowanie jako tytuł
print(s.swapcase()) #duze na male, male na duze
print(s.center(100)) #centrowanie
print(s.replace("R","D")) #zmiana znaków
print("Czy liczba:",s.isdecimal()) #sprawdzenie czy string jest liczba

print("4-ta litera:", s[3]) #pobierz 4-ta literę napisu
print("Litera przedostatnia:", s[-2]) #


