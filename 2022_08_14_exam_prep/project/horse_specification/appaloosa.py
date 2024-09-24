from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAINING_SPEED = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        new_speed = self.speed + self.TRAINING_SPEED
        self.speed = min(new_speed, self.MAX_SPEED)


a = Appaloosa("test_name", 90)

# print(a.MAX_SPEED)
# print(a.TRAINING_SPEED)
# print(a.name)
# print(a.speed)
#
# a.train()
# print(a.speed)
