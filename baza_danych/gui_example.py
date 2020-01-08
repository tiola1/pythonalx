import tkinter
import math

def pierwisatkuj():
    liczba = int(pole.get())
    pierwiastek = math.sqrt(liczba)
    wynik.configurate(text=pierwiastek)


root = tkinter.Tk()
label = tkinter.Label(master=root, text="Wpisz liczbę:")
label.grid(row=1, column=1)



pole = tkinter.Entry(master=root)
pole.grid(row=1, column=2)

buttom = tkinter.Button(master=root, text="Przelicz", command= pierwisatkuj)
buttom.grid(row=2, column=1)

wynik = tkinter.Label(master=root, text="")
wynik.grid(row=2, column=2)


root.mainloop()
print("To jest po mainloop")
