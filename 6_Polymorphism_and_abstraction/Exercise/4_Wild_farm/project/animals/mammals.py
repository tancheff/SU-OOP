from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Vegetable, Fruit]

    @property
    def gained_weight(self) -> float:
        return 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Vegetable, Meat]

    @property
    def gained_weight(self) -> float:
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00

    def make_sound(self):
        return "ROAR!!!"
