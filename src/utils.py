"""
TODO
"""

from typing import Any, Optional


def normalize_name(name : str) -> str:
    """
    Perform normalization of player names so that we can perform name matching on websites that may
    using slightly different name variations (for instance, the inclusion of "Jr." or "Sr.").
    """
    replace_strings = ["sr", "jr", "iii", "iv", "ii", ".", ",", "'", "-", " "]
    name = name.lower().strip()
    for rep in replace_strings:
        name = name.replace(rep, "")
    return name


def to_int(data : Any) -> Optional[int]:
    """
    Convert the given value to an integer if possible, otherwise return None.
    """
    if data is None:
        return None

    try:
        return int(data)
    except ValueError:
        return None
