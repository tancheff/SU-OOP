from typing import List


class Team:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Tournament:
    def __init__(self):
        self.teams: List[Team] = []

    def new_team(self, name: str):
        self.teams.append(Team(name))

    def remove_team(self, team_name):
        team = next(filter(lambda team: team.name == team_name, self.teams))
        self.teams.remove(team)

    def __repr__(self):
        result = []
        for team in self.teams:
            result.append(team.name)

        return ", ".join(result)


tournament = Tournament()

tournament.new_team("A")
tournament.new_team("B")
tournament.new_team("C")
tournament.new_team("D")

print(tournament)

tournament.remove_team("B")

print(tournament)
