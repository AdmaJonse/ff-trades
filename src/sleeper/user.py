"""
TODO
"""
from typing import Any, Optional
from src.sleeper.request import request

resource : str = "user/"

def get_user(user_id : str) -> Optional[int]:
    """
    TODO
    """
    url : str = resource + user_id
    key : str = "user_id"
    response = request(url)
    if response is not None and key in response:
        return int(response[key])
    return None


def get_user_id(username : str) -> Optional[int]:
    """
    TODO
    """
    url : str = resource + username
    key : str = "user_id"
    response = request(url)
    if response is not None and key in response:
        return int(response[key])
    return None


def get_user_leagues(user_id : int, season : int) -> Optional[Any]:
    """
    Return a list of leagues in which this user is a member.
    """
    url      : str           = resource + str(user_id) + "/leagues/nfl/" + str(season)
    response : Optional[Any] = request(url)
    if response is not None:
        return response
    return None
