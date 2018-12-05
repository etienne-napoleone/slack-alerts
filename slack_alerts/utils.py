from typing import Dict

from slack_alerts.exceptions import InvalidPayload


def merge_dicts(*args: Dict[str, str]) -> Dict[str, str]:
    merged_dict = {}
    try:
        for arg in args:
            merged_dict.update(arg)
        return merged_dict
    except (ValueError, TypeError):
        raise InvalidPayload('Could not merge dictionaries')
