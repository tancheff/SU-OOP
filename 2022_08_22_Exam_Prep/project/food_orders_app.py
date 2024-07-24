from typing import List, Dict
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.__receipt_id = 0

    @property
    def receipt_id(self):
        self.__receipt_id += 1
        return self.__receipt_id

    def register_client(self, client_phone_number: str) -> str:
        client: Client = next(filter(lambda client: client.phone_number == client_phone_number, self.clients_list),
                              None)

        if client:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *args: Meal):
        meals = [meal for meal in args if meal.__class__.__name__ in self.VALID_MEALS]
        self.menu.extend(meals)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **kwargs) -> str:
        client: Client = next(filter(lambda client: client.phone_number == client_phone_number, self.clients_list),
                              None)

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not client:
            self.clients_list.append(Client(client_phone_number))

        for meal_name, value in kwargs.items():
            meal = next(filter(lambda meal: meal.name == meal_name, self.menu), None)

            if meal not in self.menu:
                raise Exception(f"{meal_name} is not on the menu!")

            if value > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        return self.checkout_with_meals(client, **kwargs)

    def checkout_with_meals(self, client: Client, **meals_and_quantities) -> str:
        for meal_name, quantity in meals_and_quantities.items():
            meal: Meal = next(filter(lambda meal: meal.name == meal_name, self.menu), None)

            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity

            for menu_meal in self.menu:
                if menu_meal == meal:
                    menu_meal.quantity -= quantity

        return (f"Client {client.phone_number} successfully ordered "
                f"{', '.join(meal.name for meal in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client: Client = next(filter(lambda client: client.phone_number == client_phone_number, self.clients_list),
                              None)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for client_meal in client.shopping_cart:
            for menu_meal in self.menu:
                if client_meal == menu_meal:
                    menu_meal.quantity += client_meal.quantity
                    client_meal.quantity = 0

        client.bill = 0
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client: Client = next(filter(lambda client: client.phone_number == client_phone_number, self.clients_list),
                              None)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        receipt_amount = client.bill
        client.bill = 0
        client.shopping_cart.clear()

        return (f"Receipt #{self.receipt_id} with total amount of {receipt_amount:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return (f"Food Orders App has {len(self.menu)} meals on the menu "
                f"and {len(self.clients_list)} clients.")
