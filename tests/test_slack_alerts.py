import pytest

import slack_alerts as sa
from slack_alerts import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_get_alerter_ok():
    sa.alerter('https://slack.com/kek', '#test', name='test')
    assert sa.get_alerter('test')
    del sa._alerters['test']


def test_get_alerter_nok():
    with pytest.raises(sa.NoSuchAlerter):
        sa.get_alerter('test')
