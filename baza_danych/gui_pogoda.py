import tkinter
from pogoda import get_location_id, get_location_weather, weather_report


def pobierz_pogode():
    location_name= pole.get()
    location_id = get_location_id(location_name)
    weather=get_location_weather(location_id)
    report = weather_report(weather)


root = tkinter.Tk()
label = tkinter.Label(master=root, text="Wpisz miasto:")
label.grid(row=1, column=1)



pole = tkinter.Entry(master=root)
pole.grid(row=1, column=2)

buttom = tkinter.Button(master=root, text="Sprawdz", command= pobierz_pogode)
buttom.grid(row=2, column=1)

wynik = tkinter.Label(master=root, text="")
wynik.grid(row=2, column=2)


root.mainloop()
print("To jest po mainloop")
