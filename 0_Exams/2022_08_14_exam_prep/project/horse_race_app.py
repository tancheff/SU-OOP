from typing import List
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        # valid_horse_types = ["Appaloosa", "Thoroughbred"]
        horse: Horse = next(filter(lambda horse: horse.name == horse_name, self.horses), None)

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in self.VALID_HORSE_TYPES:
            return

        self.horses.append(self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey: Jockey = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys), None)

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race: HorseRace = next(filter(lambda race: race.race_type == race_type, self.horse_races), None)

        if race:
            raise Exception(f"Race {race.race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey: Jockey = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys), None)
        horse: Horse = next(filter(lambda horse: horse.__class__.__name__ == horse_type, self.horses.__reversed__()),
                            None)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse or horse.is_taken:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey: Jockey = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys), None)
        race: HorseRace = next(filter(lambda race: race.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race: HorseRace = next(filter(lambda race: race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        return self.horse_with_highest_speed(race)

    def horse_with_highest_speed(self, race: HorseRace):
        winner_jockey: Jockey = race.jockeys[0]

        for jockey in race.jockeys:
            if jockey.horse.speed > winner_jockey.horse.speed:
                winner_jockey = jockey

        return (f"The winner of the {race.race_type} race, "
                f"with a speed of {winner_jockey.horse.speed}km/h "
                f"is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}.")
