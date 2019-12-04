"""
utwórz klasę Produkt,
która będzie działać tak:
# >>>pr = Product(1, "woda", 10.99)
# >>>pr.id
# >>>1
# >>>pr.name
# >>>woda
# >>>pr.price
# >>>10.99

# >>>pr.show()
# >>> 'Woda (1), cena: 10.99'
"""


class Product:

    _NEXT_ID = 1 #atrybut klasowy

     def __init__(self, name, price):
         self.id = Product.NEXT.ID #pobiera atrybut klasowy i przypisuje go do instancji
         self.name = name
         self.price = price
         self.incr_next_id()


    @classmethod
    def incr_next_id(cls):
        cls.NEXT_ID +=1

    @classmethod
    def get_id(cls):
        return cls._NEXT_ID

     def show (self):
          return f"{self.name}, {self.id},{self.price}"


def test_product():
    pr = Product (1, "woda", 10.99)
    pr2 = Product("wóda", 10.99)
    assert pr.id == 1
    assert pr.name == 'woda'
    assert pr.price ==10.99
    assert pr2.id ==2

def test_product_show():
    pr = Product(1, 'woda', 10.99)
    assert pr.show() == "woda (1), cena: 10.99"
