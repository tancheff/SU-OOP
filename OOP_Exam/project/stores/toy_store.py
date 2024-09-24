from typing import Dict

from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    SUB_TYPE = "Toys"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)
        self.toy_models: Dict[str: [int, float]] = {}  # {model: sum(count), sum(price)}

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        sorted_products = sorted(self.products, key=lambda p: p.model)

        for product in sorted_products:
            if product.model not in self.toy_models:
                self.toy_models[product.model] = [1, product.price]

            else:
                self.toy_models[product.model][0] += 1
                self.toy_models[product.model][1] += product.price

        profit_info = self.get_estimated_profit()

        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{profit_info}\n"
                  f"**Toys for sale:")

        if not sorted_products:
            return result

        product_details = [f"{model}: {count}pcs, average price: {total_price / count:.2f}"
                           for model, (count, total_price) in self.toy_models.items()]

        return result + '\n' + '\n'.join(product_details)
