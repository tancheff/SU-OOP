from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000)

    def win(self) -> None:
        self.wins += 1
        self.advantage += 115
