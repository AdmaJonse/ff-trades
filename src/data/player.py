"""
TODO
"""

from typing import Any, Optional
from dataclasses import dataclass

from src.utils import normalize_name, to_int

@dataclass
class Player:
    """
    TODO
    """

    sleeper_id    : int           = 0
    rotowire_id   : Optional[int] = None
    rotoworld_id  : Optional[int] = None
    yahoo_id      : Optional[int] = None
    espn_id       : Optional[int] = None
    sportradar_id : Optional[int] = None

    first_name    : Optional[str] = None
    last_name     : Optional[str] = None
    full_name     : Optional[str] = None
    normal_name   : Optional[str] = None

    team          : Optional[str] = None
    position      : Optional[str] = None
    age           : Optional[int] = None
    height        : Optional[str] = None
    weight        : Optional[int] = None
    number        : Optional[int] = None
    college       : Optional[str] = None
    value         : Optional[int] = None

    def __init__(self, data : Any):
        if data is not None:
            self.sleeper_id    : int           = int(data.get("player_id"))
            self.rotowire_id   : Optional[int] = to_int(data.get("rotowire_id", None))
            self.rotoworld_id  : Optional[int] = to_int(data.get("rotoworld_id", None))
            self.yahoo_id      : Optional[int] = to_int(data.get("yahoo_id", None))
            self.espn_id       : Optional[int] = to_int(data.get("espn_id", None))
            self.sportradar_id : Optional[int] = to_int(data.get("sportradar_id", None))

            self.first_name    : Optional[str] = data.get("first_name", None)
            self.last_name     : Optional[str] = data.get("last_name", None)
            self.full_name     : Optional[str] = None
            self.normal_name   : Optional[str] = None

            self.team          : Optional[str] = data.get("team", None)
            self.position      : Optional[str] = data.get("position", None)
            self.age           : Optional[int] = to_int(data.get("age", None))
            self.height        : Optional[str] = data.get("height", None)
            self.weight        : Optional[int] = to_int(data.get("weight", None))
            self.number        : Optional[int] = to_int(data.get("number", None))
            self.college       : Optional[str] = data.get("college", None)
            self.value         : Optional[int] = 0

            if self.first_name is not None and self.last_name is not None:
                self.full_name = self.first_name + " " + self.last_name

            if self.full_name is not None:
                self.normal_name = normalize_name(self.full_name)

    def __repr__(self):
        return "Player<" + str(self.sleeper_id) + ", " + self.full_name + ">"

    def __str__(self):
        return self.full_name

    def __lt__(self, other : 'Player'):
        """
        TODO
        """
        if self.value is None:
            return True
        elif other.value is None:
            return False
        else:
            return self.value < other.value
