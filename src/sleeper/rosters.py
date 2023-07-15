"""
TODO
"""
from typing import List

from src.data.player import Player
from src.sleeper.league import get_rosters
from src.sleeper.players import get_player

def get_roster_ids(league_id : int, owner_id : int):
    """
    TODO
    """
    league_rosters = get_rosters(league_id)
    if league_rosters is not None:
        for roster in league_rosters:
            if roster["owner_id"] == str(owner_id):
                return roster
    return None


def get_roster(league_id : int, owner_id : int) -> List[Player]:
    """
    TODO
    """
    players : List[Player] = []
    roster  = get_roster_ids(league_id, owner_id)
    if roster is not None:
        for player in roster["players"]:
            if player is not None:
                data = get_player(player)
                if data is not None:
                    players.append(data)
    players.sort(reverse=True)
    return players


def get_roster_value(roster : List[Player]) -> int:
    """
    TODO
    """
    value : int = 0
    for player in roster:
        if player.value is not None:
            value += player.value
    return value
