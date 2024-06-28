from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        # for product in self.products:
        #     if product.name == product_name:
        #         return product

        # return next((p for p in self.products if p.name == product_name), None)

        return [p for p in self.products if p.name == product_name][0]

    def remove(self, product_name) -> None:
        product = self.find(product_name)
        self.products.remove(product)
        # self.products.remove(product)

    def __repr__(self) -> str:
        repository = ""
        for product in self.products:
            repository += f"{product.name}: {product.quantity}\n"

        return repository
