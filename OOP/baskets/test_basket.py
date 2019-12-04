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







