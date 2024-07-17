from abc import ABC, abstractmethod
from typing import List

from equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self,
                 name: str,
                 country: str,
                 advantage: int,
                 budget: float
                 ):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("Team name cannot be empty!")

        self.__name = value


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value


    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([eq.price for eq in self.equipment])
        total_team_protection = sum([eq.protection for eq in self.equipment])

        if len(self.equipment) == 0:
            avg_team_protection = 0
        else:
            avg_team_protection = total_team_protection / len(self.equipment)

        return (f"Name: {self.__name}\n"
                f"Country: {self.__country}\n"
                f"Advantage: {self.__advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n"
                f"Average Protection: {avg_team_protection:.0f}\n")


