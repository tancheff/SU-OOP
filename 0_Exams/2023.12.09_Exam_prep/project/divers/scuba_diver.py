from math import ceil

from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        self.oxygen_level = max(self.oxygen_level - ceil(time_to_catch*0.3), 0)

        # възможно е да е:
        # self.oxygen_level = max(ceil(self.oxygen_level - time_to_catch*0.3), 0)

    def renew_oxy(self):
        self.oxygen_level = 540
