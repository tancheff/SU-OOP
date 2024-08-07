from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        equipment: BaseEquipment = next(filter(lambda equipment: equipment.__class__.__name__ == equipment_type, self.equipment), None)
        team: BaseTeam = next(filter(lambda team: team.name == team_name, self.teams), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        team: BaseTeam = next(filter(lambda team: team.name == team_name, self.teams), None)

        if not team:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:
        count = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str) -> str:
        team_1: BaseTeam = next(filter(lambda team: team.name == team_name1, self.teams), None)
        team_2: BaseTeam = next(filter(lambda team: team.name == team_name2, self.teams), None)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_points = team_1.advantage + sum([equipment.protection for equipment in team_1.equipment])
        team_2_points = team_2.advantage + sum([equipment.protection for equipment in team_2.equipment])

        if team_1_points > team_2_points:
            team_1.win()
            return f"The winner is {team_1.name}."

        elif team_1_points < team_2_points:
            team_2.win()
            return f"The winner is {team_2.name}."

        else:
            return "No winner in this game."

    def get_statistics(self) -> str:
        self.teams.sort(key=lambda team: team.wins, reverse=True)

        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:\n"
        ]

        teams_info = '\n'.join(team.get_statistics() for team in self.teams)

        return '\n'.join(result) + teams_info
