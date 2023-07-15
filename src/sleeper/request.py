"""
The base Sleeper API request.
"""

from typing import Any, Optional
import requests

from src.logger import log

base_url : str = "https://api.sleeper.app/v1/"

def request(resource : str) -> Optional[Any]:
    """
    TODO
    """
    url : str = base_url + resource
    response : requests.Response = requests.get(url, timeout=10)
    if response.ok:
        return response.json()
    else:
        log.error("Invalid response from: " + url)
        return None
