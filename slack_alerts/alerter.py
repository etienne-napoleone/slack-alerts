from typing import Dict

import requests

from slack_alerts.exceptions import CouldNotSendAlert


class Alerter:
    """Alerter class, an alert manager.

    This class holds the repetitive configuration.
    This way you can instanciate it once and not need to always pass
    the url and channel.
    """

    def __init__(self, url: str, channel: str, username: str = __name__,
                 icon_emoji: str = None, timeout: int = 1) -> None:
        self.url = url
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji
        self.timeout = timeout

    def critical(self, message: str, title: str = None):
        """Preformated critical message."""
        pass

    def warning(self, message: str, title: str = None):
        """Preformated warning message."""
        pass

    def info(self, message: str, title: str = None):
        """Preformated warning message."""
        pass

    def ok(self, message: str, title: str = None):
        """Preformated ok message."""
        pass

    def _send(self, data: Dict[str, str]) -> None:
        """Send the request to the Slack webhook."""
        try:
            r = requests.post(self.url, data=data, timeout=self.timeout)
            r.raise_for_status()
        except (requests.exceptions.RequestException,
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.URLRequired,
                requests.exceptions.TooManyRedirects,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout) as e:
            raise CouldNotSendAlert('Alert was not sent due to {}'
                                    .format(e))
