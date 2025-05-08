from typing import List

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    PLANT_TYPES = {"Flower": Flower, "LeafPlant": LeafPlant}
    CLIENT_TYPES = {"RegularClient": RegularClient, "BusinessClient": BusinessClient}

    def __init__(self):
        self.income: float = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []
        # self.orders_count = 0

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str) -> str:
        if plant_type not in self.PLANT_TYPES:
            raise ValueError("Unknown plant type!")

        self.plants.append(self.PLANT_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data))

        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        client: BaseClient = next(filter(lambda c: c.phone_number == client_phone_number, self.clients), None)

        if client_type not in self.CLIENT_TYPES:
            raise ValueError("Unknown client type!")

        if client:
            raise ValueError("This phone number has been used!")

        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_phone_number))

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int) -> str:
        client: BaseClient = next(filter(lambda c: c.phone_number == client_phone_number, self.clients), None)
        plant: BasePlant = next(filter(lambda p: p.name == plant_name, self.plants), None)
        same_type_plants: List[BasePlant] = list(filter(lambda p: p.name == plant_name, self.plants))

        if not client:
            raise ValueError("Client not found!")

        if not plant:
            raise ValueError("Plants not found!")

        if len(same_type_plants) < plant_quantity:
            return "Not enough plant quantity."

        order_amount = self.perform_sale(same_type_plants, client, plant_quantity)
        # self.orders_count += 1

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount}"

    def perform_sale(self, plants: List[BasePlant], client: BaseClient, quantity: int) -> int:
        client.update_total_orders()
        client.update_discount()
        order_amount = 0

        for plant in plants[:quantity]:
            order_amount += plant.price

        self.plants = plants[quantity:]

        return order_amount

    def remove_plant(self, plant_name: str):
        plant: BasePlant = next(filter(lambda p: p.name == plant_name, self.plants), None)

        if not plant:
            return "No such plant name."

        self.plants.remove(plant)

        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        removed_clients: List[BaseClient] = list(filter(lambda c: c.total_orders == 0, self.clients))

        self.clients = [c for c in self.clients if c not in removed_clients]

        return f"{len(removed_clients)} client/s removed."

    def shop_report(self):
        report = ["~Flower Shop Report~"]
        report.extend([f"Income: {self.income:.2f}"])
        report.extend([f"Count of orders: {sum([client.total_orders for client in self.clients])}"])
        report.extend([f"~~Unsold plants: {len(self.plants)}~~"])

        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1

        sorted_plant_counts = (f"{plant_name}: {count}" for plant_name, count in sorted(
            plant_counts.items(), key=lambda x: (-x[1], x[0])
        ))
        report.extend(sorted_plant_counts)

        report.extend([f"~~Clients number: {len(self.clients)}~~"])

        sorted_clients = (client.client_details() for client in sorted(
            self.clients, key=lambda c: (-c.total_orders, c.phone_number)
        ))
        report.extend(sorted_clients)

        return "\n".join(report)



