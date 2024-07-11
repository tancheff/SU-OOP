from typing import List, Tuple

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Tuple[Player]) -> str:
        players_added: List[Player] = []

        for player in args:
            if player not in self.players:
                players_added.append(player)
                self.players.append(player)

        return f"Successfully added: {', '.join([player.name for player in players_added])}"

    def add_supply(self, *args: Tuple[Supply]) -> None:
        [self.supplies.append(supply) for supply in args]

    def sustain(self, player_name: str, sustenance_type: str) -> str or None:
        player = next(filter(lambda player: player.name == player_name, self.players), None)
        # supply = next(filter(lambda supply: supply.name == sustenance_type, self.supplies), None)

        if sustenance_type not in ["Food", "Drink"]:
            return

        if not player:
            return

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        if sustenance_type not in [supply.type for supply in self.supplies]:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        for i in range(-1, len(self.supplies) * (-1) - 1, -1):
            if self.supplies[i].type == sustenance_type:
                sustenance = self.supplies.pop(i)

                if (player.stamina + sustenance.energy) > 100:
                    player.stamina = 100
                else:
                    player.stamina += sustenance.energy

                return f"{player_name} sustained successfully with {sustenance.name}."

    def check_stamina(self, player_1: Player, player_2: Player) -> str or None:
        message: List[str] = []

        if player_1.stamina == 0:
            message.append(f"Player {player_1.name} does not have enough stamina.")

        if player_2.stamina == 0:
            message.append(f"Player {player_2.name} does not have enough stamina.")

        return '\n'.join(message) if message else None

    def check_negative_stamina(self, player_1, player_2):
        if player_1.stamina <= 0:
            return f"Winner: {player_2.name}"

        if player_2.stamina <= 0:
            return f"Winner: {player_1.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = next(filter(lambda player: player.name == first_player_name, self.players))
        player_2 = next(filter(lambda player: player.name == second_player_name, self.players))

        # implementing additional method:
        if self.check_stamina(player_1, player_2):
            return self.check_stamina(player_1, player_2)

        if player_1.stamina < player_2.stamina:
            # 1st attack:
            player_2.stamina = max(player_2.stamina - player_1.stamina / 2, 0)
            self.check_negative_stamina(player_1, player_2)

            # 2nd attack:
            player_1.stamina = max(player_1.stamina - player_2.stamina / 2, 0)
            self.check_negative_stamina(player_1, player_2)

        else:
            # 1st attack:
            player_1.stamina = max(player_1.stamina - player_2.stamina / 2, 0)
            self.check_negative_stamina(player_1, player_2)

            # 2nd attack:
            player_2.stamina = max(player_2.stamina - player_1.stamina / 2, 0)
            self.check_negative_stamina(player_1, player_2)

        if player_1.stamina > player_2.stamina:
            return f"Winner: {player_1.name}"
        else:
            return f"Winner: {player_2.name}"

    def next_day(self):
        for player in self.players:
            if (player.stamina - player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            had_food = False
            had_drink = False

            for supply in self.supplies:
                if had_drink and had_food:
                    break

                if supply.type == "Food" and not had_food:
                    if (player.stamina + supply.energy) > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy
                    self.supplies.remove(supply)
                    had_food = True

                if supply.type == "Drink" and not had_drink:
                    if (player.stamina + supply.energy) > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy
                    self.supplies.remove(supply)
                    had_drink = True

    def __str__(self):
        result = []

        for player in self.players:
            result.append(player.__str__())

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# third_player = Player("Kiril", 30)
# # fourth_player = Player('Kiril', 29)
# c = Controller()
# print(c.add_player(first_player, second_player, third_player))
# # for player in c.players:
# #     print(player)
