from produkt import Product
from baskets import Basket


class TestBasket:

    def test_create_basket(self):
        basket = Basket()
        assert True

    def test_add_product_to_basket(self):
        basket = Basket()
        product = Produkt("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.items) == 1
        basket.add_product(product2,2)
        assert len(basket.items) == 2

    def test_count_total_price(self):
        basket = Basket()
        product = Produkt("Woda", 10)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50
        product2 = Product(product2, 2)
        assert basket.count_total_price() == 54


    def test_generate_report(self):
        basket = Basket()
        product = Product ("Woda", 10)
        basket.add_product(product, 5)
        expected = """ Produkty w koszyku:
-Woda (5), cena: 10 x 5
-Chleb (6), cena: 2 x 2
W sumie: 54"""
        assert basket.generate_report() == expected





