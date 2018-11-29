import pytest

from slack_alerts import utils
from slack_alerts.exceptions import InvalidPayload

PAYLOAD_ONE = {'one': 'test'}
PAYLOAD_TWO = {'two': 'test'}


def test_merge_dicts_with_dicts():
    assert len(utils.merge_dicts(PAYLOAD_ONE, PAYLOAD_TWO)) == 2


def test_merge_dicts_raise_with_other_type():
    with pytest.raises(InvalidPayload, match='Could not merge dictionaries'):
        utils.merge_dicts(PAYLOAD_ONE, 2)
