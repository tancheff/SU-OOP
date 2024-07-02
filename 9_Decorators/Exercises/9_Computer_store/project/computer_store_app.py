from typing import List

from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp(DesktopComputer, Laptop):
    @property
    def valid_types(self):
        return ["Desktop Computer", "Laptop"]

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.warehouse: List[str] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        self.configure_computer(processor, ram)


    def build_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        pass
