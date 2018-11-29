import os

# import pytest

import slack_alerts as sa
from slack_alerts import __version__

URL = os.getenv('SLACK_WEBHOOK_URL', 'https://slack.com/url')
CHANNEL = os.getenv('SLACK_WEBHOOK_CHANNEL', 'alert')


def test_version():
    assert __version__ == '0.1.0'


def test_instanciate_alerter():
    assert isinstance(sa.Alerter(URL, CHANNEL), sa.Alerter)
