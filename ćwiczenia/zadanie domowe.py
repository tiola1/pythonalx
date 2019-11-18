from random import shuffle


osoby = [ 'marek', 'przemek', 'michal', 'kamila']
osoby2 = ['marek', 'przemek', 'michal', 'kamila']
osoby2 = ['kamila', 'miachal', 'przemek', 'marek']


def is_in_same_position(lista1, lista2):
    for i, os in enumerate(lista1):
        if os == lista2[i]:
            return True
    return False
print( is_in_same_position(osoby, osoby2))



#tutaj wasza magaia:

while is_in_same_position(osoby, osoby2):
    i +=1
    print("cos się powtarza")
    shuffle(osoby)
   # shuffle(osoby2)


