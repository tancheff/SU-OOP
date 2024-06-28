from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        # if self.__budget >= price:
        #     if self.__animal_capacity > len(self.animals):
        #         self.animals.append(animal)
        #         self.__budget -= price
        #         return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        #     else:
        #         return "Not enough space for animal"
        # else:
        #     return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        # try:
        #     worker = [w for w in self.workers if w.name == worker_name][0]
        # except IndexError:
        #     return f"There is no {worker_name} in the zoo"

        try:
            worker = next(filter(lambda w: w.name == worker.name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salary = sum([w.salary for w in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return (f"You payed your workers. They are happy. "
                    f"Budget left: {self.__budget}")
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animal_cost = sum([a.money_for_care for a in self.animals])
        if self.__budget >= total_animal_cost:
            self.__budget -= total_animal_cost
            return (f"You tended all the animals. They are happy. "
                    f"Budget left: {self.__budget}")
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)}\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result


