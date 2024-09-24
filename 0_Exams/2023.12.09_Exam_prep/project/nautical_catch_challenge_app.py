from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        diver: BaseDiver = next(filter(lambda diver: diver.name == diver_name, self.divers), None)

        if diver:
            return f"{diver_name} is already a participant."

        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        fish: BaseFish = next(filter(lambda fish: fish.name == fish_name, self.fish_list), None)

        if fish:
            return f"{fish_name} is already permitted."

        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        diver: BaseDiver = next(filter(lambda diver: diver.name == diver_name, self.divers), None)
        fish: BaseFish = next(filter(lambda fish: fish.name == fish_name, self.fish_list), None)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        return self.oxygen_level_comparison(diver, fish, is_lucky)

    def oxygen_level_comparison(self, diver: BaseDiver, fish: BaseFish, is_lucky: bool) -> str:
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            self.zero_oxygen_level_handling(diver)
            return f"{diver.name} missed a good {fish.name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                self.zero_oxygen_level_handling(diver)
                return f"{diver.name} missed a good {fish.name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    def zero_oxygen_level_handling(self, diver: BaseDiver):
        if diver.oxygen_level == 0:
            diver.update_health_status()

    def health_recovery(self):
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver: BaseDiver = next(filter(lambda diver: diver.name == diver_name, self.divers), None)

        return (f"**{diver_name} Catch Report**\n"
                f"{'\n'.join(fish.fish_details() for fish in diver.catch)}")

    def competition_statistics(self):
        sorted_divers: List[BaseDiver] = sorted(filter(lambda d: d.has_health_issue is False, self.divers),
                                                key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        return (f"**Nautical Catch Challenge Statistics**\n"
                f"{'\n'.join([diver.__str__() for diver in sorted_divers])}")
