"""
TODO
"""
from datetime import datetime
from src.utils import normalize_name
from src.value_strategy import ValueStrategy

class Evaluator:
    """
    TODO
    """

    def __init__(self, strategy : ValueStrategy) -> None:
        """
        TODO
        """
        self._strategy = strategy


    @property
    def strategy(self) -> ValueStrategy:
        """
        Accessor for the strategy for determining player value.
        """
        return self._strategy


    @strategy.setter
    def strategy(self, strategy : ValueStrategy) -> None:
        """
        Mutator for the strategy for determining player value.
        """
        self._strategy = strategy


    def get_player_value(self, player : str, date : datetime = datetime.now()) -> int:
        """
        Return the value for the given player as determined by the current strategy. Optionally, 
        provide a date to support historical player values.
        """
        player = normalize_name(player)
        return self._strategy.get_player_value(player, date)
