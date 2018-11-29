import os

import pytest

import slack_alerts as sa
from slack_alerts import __version__
from slack_alerts.exceptions import CouldNotSendAlert


URL = os.getenv('SLACK_WEBHOOK_URL')
URL_INVALID = 'test.test/test'
RAW_MESSAGE = {'text': 'testing: v{}'.format(__version__)}
RAW_MESSAGE_INVALID = {'test': 'testing: v{}'.format(__version__)}


def test_repr():
    a = sa.Alerter(URL)
    assert a.__repr__() == 'Alerter for channel (default)'


def test_send_with_good_url():
    a = sa.Alerter(URL)
    a._send(RAW_MESSAGE)


def test_send_with_invalid_url():
    a = sa.Alerter(URL_INVALID)
    with pytest.raises(CouldNotSendAlert, match=r'Request errored.*'):
        a._send(RAW_MESSAGE)


def test_send_with_invalid_response():
    a = sa.Alerter(URL)
    with pytest.raises(CouldNotSendAlert, match=r'Invalid response.*'):
        a._send(RAW_MESSAGE_INVALID)
