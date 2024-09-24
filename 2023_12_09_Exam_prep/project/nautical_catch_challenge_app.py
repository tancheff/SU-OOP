from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        diver: BaseDiver = next(filter(lambda d: d.name == diver_name, self.divers), None)

        if diver_type not in self.VALID_DIVER_TYPES:
            return "{diver_type} is not allowed in our competition."

        # if diver in self.divers:
        if diver:
            return f"{diver_name} is already a participant."

        self.divers.append(self.VALID_DIVER_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        fish: BaseFish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)

        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        # if fish in self.fish_list:
        if fish:
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.VALID_FISH_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver: BaseDiver = next(filter(lambda d: d.name == diver_name, self.divers), None)
        fish: BaseFish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        return self.oxygen_level_comparison(diver, fish, is_lucky)

    def oxygen_level_comparison(self, diver: BaseDiver, fish: BaseFish, is_lucky: bool):
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver.name} missed a good {fish.name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver.name} hits a {fish.points}pt. {fish.name}."
            if not is_lucky:
                diver.miss(fish.time_to_catch)
                return f"{diver.name} missed a good {fish.name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    def health_recovery(self):
        divers_to_recover = [diver for diver in self.divers if diver.has_health_issue]

        for diver in divers_to_recover:
            diver.renew_oxy()
            diver.update_health_status()

        return f"Divers recovered: {len(divers_to_recover)}"


























