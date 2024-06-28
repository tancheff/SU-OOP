from project.pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []  # [Pokemon("pikachu", 100), Pokemon("charizard", 80), ...]

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details}"
            # return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        except IndexError:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        pokemon_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])
        return f"Pokemon Trainer {self.name}\n" + \
            f"Pokemon count {len(self.pokemons)}\n" + \
            f"{pokemon_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
