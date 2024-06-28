from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    # @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

