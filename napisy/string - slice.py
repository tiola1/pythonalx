#
# array slicing
#
s= "Ruda tańczy jak szalona!"


arr=s.split (" ")
print(arr[0]) # pierwszsy element listy

print(s[100])

print(s[0:16:2]) #co 2-znak od indeksu 0 do 15 włącznie
print(s[::3])  #caly string co 3ci znak

#grande finale
# rewerse w Pythonie - uzupelnic rewerse



a = "Hello"
b = "ALX"
print("Hello + World!")

print(f"{a} {b} {1+2}.")
print ("{} {} {}".format(a, b, 1+6))

x = input("Podaj wartość x")   # wszystko co jest zwracane z inp-utu jest zwracane na napis
x = int(x)
print(x, type(x))


