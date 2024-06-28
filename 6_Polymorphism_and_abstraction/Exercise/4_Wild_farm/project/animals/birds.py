from typing import List
from project.food import Food, Meat, Seed, Vegetable, Fruit

from project.animals.animal import Bird


class Owl(Bird):
    @property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self) -> list:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35

    def make_sound(self):
        return "Cluck"
