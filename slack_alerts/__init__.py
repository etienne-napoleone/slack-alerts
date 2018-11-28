from slack_alerts.alerter import Alerter
from slack_alerts.exceptions import NoSuchAlerter

__version__ = '0.1.0'

_alerters = {}


def alerter(url: str, channel: str, name: str = __name__,
            username: str = __name__, icon_emoji: str = None) -> Alerter:
    _alerters[name] = Alerter(url=url, channel=channel, username=username,
                              icon_emoji=icon_emoji)
    return _alerters[name]


def get_alerter(name: str = __name__) -> Alerter:
    try:
        return _alerters[name]
    except KeyError:
        raise NoSuchAlerter('Could not find an alerter named {}'
                            .format(name))
