"""
This module provides the interface for a strategy for determining player value.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class ValueStrategy(ABC):
    """
    This class provides the interface for a strategy for determining player value.
    """

    @abstractmethod
    def get_player_value(self, player : str, date : datetime = datetime.now()) -> int:
        """
        Return the value of the given player as an integer. Optionally provide the date of the value
        to support historical player values.
        """
