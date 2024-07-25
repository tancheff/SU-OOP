from project.shopping_cart import ShoppingCart
from unittest import TestCase


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("TestName", 11.11)
        self.cart.products = {"product_1": 1, "product_2": 2, "product_3": 3}

    def test_initialisation(self):
        self.assertEqual(self.cart.shop_name, "TestName")

        self.assertEqual(self.cart.products,
                         {"product_1": 1, "product_2": 2, "product_3": 3})

    def test_shop_name_setter_exception_numbers(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "123123"

        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ex.exception))

    def test_shop_name_setter_exception_capital_letter(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "test_name"

        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ex.exception))

    def test_shop_name_setter_successful(self):
        self.cart.shop_name = "TestTest"
        self.assertEqual(self.cart.shop_name, "TestTest")

    def test_add_to_cart_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("product_0", 101.1)

        self.assertEqual("Product product_0 cost too much!",
                         str(ex.exception))

    def test_add_to_cart_successful(self):
        self.assertEqual(self.cart.add_to_cart("product_0", 10),
                         "product_0 product was successfully added to the cart!")

        self.assertEqual(self.cart.products,
                         {"product_0": 10, "product_1": 1, "product_2": 2, "product_3": 3})

    def test_remove_from_cart_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.remove_from_cart("product_0")

        self.assertEqual("No product with name product_0 in the cart!",
                         str(ex.exception))

    def test_remove_from_cart_successful(self):
        self.assertEqual(self.cart.remove_from_cart("product_1"),
                         "Product product_1 was successfully removed from the cart!")

        self.assertEqual(self.cart.products, {"product_2": 2, "product_3": 3})

    def test_add(self):
        cart_2 = ShoppingCart("NewTestName", 20.00)
        cart_2.products = {"product_9": 9}

        new_shop_name = f"{self.cart.shop_name}{cart_2.shop_name}"
        new_budget = self.cart.budget + cart_2.budget
        new_shopping_cart = ShoppingCart(new_shop_name, new_budget)
        new_shopping_cart.products.update(**self.cart.products)
        new_shopping_cart.products.update(**cart_2.products)

        self.assertEqual(self.cart.__add__(cart_2).shop_name, new_shopping_cart.shop_name)
        self.assertEqual(self.cart.__add__(cart_2).products, new_shopping_cart.products)
        self.assertEqual(self.cart.__add__(cart_2).budget, new_shopping_cart.budget)

    def test_buy_products_exception(self):
        self.cart.budget = 5
        total_sum = sum(self.cart.products.values())

        with self.assertRaises(ValueError) as ex:
            self.cart.buy_products()

        self.assertEqual(
            f"Not enough money to buy the products! Over budget with {total_sum - self.cart.budget:.2f}lv!",
            str(ex.exception))

        self.assertEqual(self.cart.products, {"product_1": 1, "product_2": 2, "product_3": 3})

    def test_buy_products_successfully(self):
        total_sum = sum(self.cart.products.values())

        self.assertEqual(self.cart.buy_products(),
                         f"Products were successfully bought! Total cost: {total_sum:.2f}lv.")
