from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    BASE_OXYGEN = 120

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.BASE_OXYGEN)
        self.name = name

    def miss(self, time_to_catch: int):
        self.oxygen_level -= round(time_to_catch*0.6)

        if self.oxygen_level < 0:
            self.oxygen_level = 0

        # if self.oxygen_level < time_to_catch:
        #     self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.BASE_OXYGEN
