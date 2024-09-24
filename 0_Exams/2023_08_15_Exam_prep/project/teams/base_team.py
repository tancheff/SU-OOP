from abc import ABC, abstractmethod
from math import floor
from statistics import mean
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
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

    def get_statistics(self) -> str:
        # avg_team_protection = floor(mean(equipment.protection for equipment in self.equipment))
        avg_team_protection = floor(sum(equipment.protection for equipment in self.equipment) / len(self.equipment)) \
            if self.equipment else 0
        result = [
            f"Name: {self.name}",
            f"Country: {self.country}",
            f"Advantage: {self.advantage} points",
            f"Budget: {self.budget:.2f}EUR",
            f"Wins: {self.wins}",
            f"Total Equipment Price: {sum(equipment.price for equipment in self.equipment):.2f}",
            f"Average Protection: {avg_team_protection}"

        ]
        return "\n".join(result)
