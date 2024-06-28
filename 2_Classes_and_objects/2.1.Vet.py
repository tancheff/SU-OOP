from typing import List


class Vet:
    ANIMALS = []
    SPACE = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.SPACE > len(Vet.ANIMALS):
            self.animals.append(animal_name)
            Vet.ANIMALS.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in Vet.ANIMALS:
            Vet.ANIMALS.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return (f"{self.name} has {len(self.animals)} animals. "
                f"{Vet.SPACE - len(Vet.ANIMALS)} space left in clinic")


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
