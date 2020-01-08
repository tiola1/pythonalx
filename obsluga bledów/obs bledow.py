lista = [1, 0, 10, 'a']  # comment

for i in lista:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("dzielisz przez zero")
    except TypeError:
        print("Dzielisz przez cos co nie jest liczba")
    except:
        pass
