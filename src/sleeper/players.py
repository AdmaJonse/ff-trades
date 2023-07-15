"""
TODO
"""

from typing import Optional

from src import data_store
from src.data.player import Player
from src.sleeper.request import request
from src.utils import normalize_name

def get_players():
    """
    TODO
    """
    url : str = "players/nfl"
    response = request(url)
    if response is not None:
        return response
    return None


def parse_players() -> None:
    """
    TODO
    """
    players = get_players()
    if players is not None:
        for player_id in players:
            if player_id.isdigit():
                data = players[player_id]
                name = normalize_name(data["first_name"] + " " + data["last_name"])
                data_store.players[name] = Player(data)


def get_player(sleeper_id : int) -> Optional[Player]:
    """
    TODO
    """
    for player in data_store.players.values():
        if int(player.sleeper_id) == int(sleeper_id):
            return player
    return None


def get_player_name(player_id : int) -> str:
    """
    TODO
    """
    player = get_player(player_id)
    if player is not None:
        return player.full_name
    return ""
