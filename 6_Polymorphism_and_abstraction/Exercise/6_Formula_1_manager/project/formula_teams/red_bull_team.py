from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1_500_000,
                2: 800_000
            },
            "Honda": {
                1: 20_000,
                10: 10_000
            }
        }

    @property
    def expenses(self):
        return 250_000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for positions in self.sponsors.values():
            for pos in positions:
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        revenue -= self.expenses
        self.budget += revenue

        return (f"The revenue after the race is {revenue}$. "
                f"Current budget {self.budget}$")
