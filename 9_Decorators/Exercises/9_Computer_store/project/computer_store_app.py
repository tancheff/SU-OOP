from typing import List

from computer_types.computer import Computer
from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTERS = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, procesor: str, ram: int) -> str:
        try:
            computer = self.VALID_COMPUTERS[type_computer](manufacturer, model, procesor, ram)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(procesor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer.__repr__()} sold for {client_budget}$."
            else:
                raise Exception(f"Sorry, we don't have a computer for you.")


