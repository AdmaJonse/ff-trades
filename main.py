"""
TODO
"""

from typing import Any, List, Tuple, Optional
from tabulate import tabulate

from src.data.player import Player
from src.logger import log
from src.sleeper import players, league, user, rosters
from src.evaluator import Evaluator
from src import ktc

if __name__ == '__main__':

    players.parse_players()
    evaluator : Evaluator = Evaluator(ktc.KeepTradeCutValue())

    # Select the user we want to analyze
    #username : str          = input("Enter Sleeper username: ")
    username : str = "AdamJones"
    user_id  : Optional[int] = user.get_user_id(username)

    if user_id is None:
        log.error("The user account does not exist.")
        exit()

    print("username: " + username)
    print("user ID:  " + str(user_id))
    leagues : Optional[Any] = user.get_user_leagues(user_id, 2023)
    if leagues is None or len(leagues) < 1:
        log.error("The user is not in any leagues")
        exit()

    # TODO: Get the season for the league (automate by checking player seasons or league seasons?)

    # Select the league we want to analyze
    print("Select a league from the following list: ")
    for (index, item) in enumerate(leagues, start=1):
        print(str(index) + ". " + item["name"])
    league_index : int = int(input("Enter the league index: ")) - 1
    if league_index < len(leagues):
        current_league : Any = leagues[league_index]
        league_id      : int = current_league["league_id"]
        print(current_league["name"] + ": " + str(league_id))
    else:
        log.error("This is not a valid index.")
        exit()

    # List your roster
    league_rosters : List[Tuple[List[Player], int]] = []
    for owner_id in league.get_all_users(league_id):
        roster : List[Player] = rosters.get_roster(league_id, owner_id)
        value  : int          = rosters.get_roster_value(roster)
        league_rosters.append((roster, value))

    league_rosters.sort(key=lambda tup: tup[1], reverse=True)

    for roster_value in league_rosters:
        print("Total Value: " + str(roster_value[1]))
        print(tabulate(roster_value[0], headers="keys"))
