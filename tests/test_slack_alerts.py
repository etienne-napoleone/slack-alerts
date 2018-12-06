import slack_alerts as sa
from slack_alerts import __version__

URL = 'test'


def test_version():
    assert __version__ == '1.0.0'


def test_instanciate_alerter():
    assert isinstance(sa.Alerter(URL), sa.Alerter)
