from typing import List

from equipment.base_equipment import BaseEquipment
from equipment.elbow_pad import ElbowPad
from equipment.knee_pad import KneePad
from teams.base_team import BaseTeam
from teams.indoor_team import IndoorTeam
from teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAMS = {
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

    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type in self.VALID_EQUIPMENT:
            new_equipment = self.VALID_EQUIPMENT[equipment_type]()
            self.equipment.append(new_equipment)
            return f"{equipment_type} was successfully added."

        raise Exception("Invalid equipment type!")

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid type!")

        if self.capacity <= len(self.teams):
            return f"Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        team = next(filter(lambda team: team.name == team_name, self.teams))
        equipment = next(filter(lambda equipment: equipment.__class__.__name__ == equipment_type, self.equipment))

        if team.budget >= equipment.price:
            team.equipment.append(equipment)
            team.budget -= equipment.price

            self.equipment.remove(equipment)

            return f"Successfully sold {equipment_type} to {team.name}."

        return "Budget is not enough!"

    def remove_team(self, team_name: str) -> str:
        team = next(filter(lambda team: team.name == team_name, self.teams), None)
        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:
        number_of_changed_equipment = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def calculate_team_points(self, team: BaseTeam):
        protection_points = 0
        for equipment in team.equipment:
            protection_points += equipment.protection

        advantage_points = team.advantage

        total_points = protection_points + advantage_points

        return total_points

    def play(self, team_name1: str, team_name2: str) -> str:
        team1 = next(filter(lambda team: team.name == team_name1, self.teams))
        team2 = next(filter(lambda team: team.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            return "Game cannot start! Team types mismatch!"

        team1_points = self.calculate_team_points(team1)
        team2_points = self.calculate_team_points(team2)

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        elif team1_points < team2_points:
            team2.win()
            return f"The winner is {team2.name}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:\n")

        self.teams.sort(key=lambda team: -team.wins)

        for team in self.teams:
            result += team.get_statistics()

        return result








            

