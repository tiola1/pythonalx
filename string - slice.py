#
# arraz slicing
#
s= "Ruda tańczy jak szalona!"


arr=s.split (" ")
print(arr[0]) # pierwszsy element listy

print(s[0:16:2]) #co 2-znak od indeksu 0 do 15 włącznie
print(s[::3])  #caly string co 3ci znak

#grande finale
# rewerse w Pythonie
print(s.[::-1])
