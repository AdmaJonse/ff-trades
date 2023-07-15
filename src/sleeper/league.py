"""
TODO
"""

from src.sleeper.request import request

resource : str = "league/"

def get_all_users(league_id : int) -> list[int]:
    """
    TODO
    """
    url   : str = resource + str(league_id) + "/users"
    users : list[int] = []
    response = request(url)
    if response is not None:
        for user in response:
            users.append(user["user_id"])
    return users


def get_rosters(league_id : int):
    """
    TODO
    """
    url : str = resource + str(league_id) + "/rosters"
    response = request(url)
    if response is not None:
        return response
    return None
