from collections import defaultdict
from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {
        "Chair": Chair,
        "HobbyHorse": HobbyHorse
    }

    VALID_STORES = {
        "FurnitureStore": FurnitureStore,
        "ToyStore": ToyStore
    }

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS:
            raise Exception("Invalid product type!")

        # self.products.append(self.VALID_PRODUCTS[product_type](model, price))
        # product_sub_type = self.VALID_PRODUCTS[product_type].sub_type

        product_class = self.VALID_PRODUCTS[product_type]
        product = product_class(model, price)
        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        # self.stores.append(self.VALID_STORES[store_type](name, location))

        store_class = self.VALID_STORES[store_type]
        store = store_class(name, location)
        self.stores.append(store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        return self.match_products_to_store(store, *products)

    def match_products_to_store(self, store: BaseStore, *products: BaseProduct):
        items_sold = 0
        total_price = 0

        for product in products:
            if product.sub_type == store.SUB_TYPE:
                items_sold += 1
                total_price += product.price
                store.capacity -= 1
                store.products.append(product)
                self.products.remove(product)

        self.income += total_price

        if items_sold > 0:
            return f"Store {store.name} successfully purchased {items_sold} items."
        else:
            return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store: BaseStore = next(filter(lambda store: store.name == store_name, self.stores), None)

        if not store:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        products_count = 0

        for product in self.products:
            if product.model == product_model:
                product.discount()
                products_count += 1

        return f"Discount applied to {products_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store: BaseStore = next(filter(lambda store: store.name == store_name, self.stores), None)

        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        unsold_products = defaultdict(int)

        for product in self.products:
            unsold_products[product.model] += 1

        product_stats = "\n".join(f"{model}: {count}" for model, count in sorted(unsold_products.items()))

        store_names = "\n".join(store.name for store in sorted(self.stores, key=lambda s: s.name))
        total_net_price = sum(product.price for product in self.products)

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            f"***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_net_price:.2f}",
            product_stats,
            f"***Partner Stores: {len(self.stores)}***",
            store_names
        ]

        return "\n".join(line for line in result if line)
