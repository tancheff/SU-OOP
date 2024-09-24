from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    BASE_OXYGEN = 540

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.BASE_OXYGEN)
        self.name = name

    def miss(self, time_to_catch: int):
        self.oxygen_level -= round(time_to_catch*0.3)

        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.BASE_OXYGEN
