from typing import Optional

from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    VALID_TEAMS = {
        "Red Bull": RedBullTeam,
        "Mercedes": MercedesTeam
    }

    def __init__(self):
        self.red_bull_team: Optional[RedBullTeam] = None
        self.mercedes_team: Optional[MercedesTeam] = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name in self.VALID_TEAMS:
            class_instance = self.VALID_TEAMS[team_name]

            if team_name == list(self.VALID_TEAMS.keys())[0]:
                self.red_bull_team = class_instance(budget)
            else:
                self.mercedes_team = class_instance(budget)

            return f"{team_name} has joined the new F1 season."

        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        better_pos = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{better_pos} is ahead at the {race_name} race.")
