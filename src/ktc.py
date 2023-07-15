"""
TODO
"""
from datetime import datetime
from typing import Dict

from bs4 import BeautifulSoup
import requests

from src import data_store
from src.logger import log
from src.utils import normalize_name
from src.value_strategy import ValueStrategy

URL : str = "https://keeptradecut.com/dynasty-rankings?filters=QB|WR|RB|TE|RDP"

class KeepTradeCutValue(ValueStrategy):
    """
    TODO
    """

    def __init__(self) -> None:
        self._values : Dict[str, int] = {}
        self.parse_ktc()


    def parse_ktc(self):
        """
        TODO
        """
        data    = requests.get(URL, timeout=10)
        players = BeautifulSoup(data.text, features='lxml').select('div[id=rankings-page-rankings] > div')

        for player in players:
            player_data = player.select('div[class=player-name] > p > a')[0]
            #pid         = player_data.get('href').split('/')[-1]
            name        = normalize_name(player_data.text)
            value       = int(player.select('div[class=value]')[0].text.strip())
            if name in data_store.players:
                data_store.players[name].value = value
            self._values[name] = value

    # TODO: How do we account for scoring format?


    def get_player_value(self, player: str, date: datetime = datetime.now()) -> int:
        """
        Return the given player's value as determined by KeepTradeCut.
        """
        if player in self._values:
            return self._values[player]
        log.error("Could not find value for player: " + player)
        return 0
