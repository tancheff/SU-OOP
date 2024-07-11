from teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500)
        self.name = name
        self.country = country
        self.advantage = advantage

    def win(self):
        self.advantage += 145
        self.wins += 1
