from typing import List
from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        else:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:

        # if player_name not in self.players:
        #     return f"Player {player_name} is not in the guild."
        # else:
        #     self.players.remove(player_name)
        #     player_name.guild = "Unaffiliated"

        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = "Unaffiliated"

    def guild_info(self) -> str:
        all_players_info = "\n".join([p.player_info() for p in self.players])

        return (f"Guild: {self.name}\n"
                f"{all_players_info}")
