from typing import Dict

from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    SUB_TYPE = "Furniture"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)
        self.furniture_models: Dict[str: [int, float]] = {}  # {model: sum(count), sum(price)}

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        sorted_products = sorted(self.products, key=lambda p: p.model)

        for product in sorted_products:
            if product.model not in self.furniture_models:
                self.furniture_models[product.model] = [1, product.price]

            else:
                self.furniture_models[product.model][0] += 1
                self.furniture_models[product.model][1] += product.price

        profit_info = self.get_estimated_profit()

        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{profit_info}\n"
                  f"**Furniture for sale:")

        if not sorted_products:
            return result

        product_details = [f"{model}: {count}pcs, average price: {total_price / count:.2f}"
                           for model, (count, total_price) in self.furniture_models.items()]

        return result + '\n' + '\n'.join(product_details)
