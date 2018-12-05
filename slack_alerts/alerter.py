from typing import Dict

import requests

from slack_alerts.exceptions import CouldNotSendAlert, InvalidPayload
from slack_alerts.elements import attachment, attachments
from slack_alerts.utils import merge_dicts


class Alerter:
    """Alerter class, an alert manager.

    This class holds the repetitive configuration.
    This way you can instanciate it once and not need to always pass
    the url, channel and other specific configurations.
    """

    def __init__(self, url: str, channel: str = None, username: str = None,
                 icon_emoji: str = None, timeout: int = 1) -> None:
        self.url = url
        self.channel = {'channel': channel}
        self.username = {'username': username}
        self.icon_emoji = {'icon_emoji': icon_emoji}
        self.timeout = timeout

    def __repr__(self):
        return ('Alerter for channel {}'
                .format(self.channel if self.channel else '(default)'))

    def critical(self, message: str, title: str = None,
                 title_link: str = None) -> None:
        """Preformated critical message."""
        self._send(attachments(
                attachment(fallback='Critical: {}'.format(message),
                           text=message, title=title, title_link=title_link,
                           color='danger')
        ))

    def warning(self, message: str, title: str = None,
                title_link: str = None) -> None:
        """Preformated warning message."""
        self._send(attachments(
                attachment(fallback='Warning: {}'.format(message),
                           text=message, title=title, title_link=title_link,
                           color='warning')
        ))

    def info(self, message: str, title: str = None,
             title_link: str = None) -> None:
        """Preformated warning message."""
        self._send(attachments(
                attachment(fallback='Info: {}'.format(message),
                           text=message, title=title, title_link=title_link,
                           color='#CCE5FF')
        ))

    def good(self, message: str, title: str = None,
             title_link: str = None) -> None:
        """Preformated ok message."""
        self._send(attachments(
                attachment(fallback='Good: {}'.format(message),
                           text=message, title=title, title_link=title_link,
                           color='good')
        ))

    def custom(self, *args) -> None:
        """Custom message with elements."""
        self._send(attachments(*args))

    def _send(self, *args: Dict[str, str]) -> None:
        """Send the request to the Slack webhook."""
        try:
            json = merge_dicts(self.channel, self.username, self.icon_emoji,
                               *args)
            r = requests.post(self.url, json=json, timeout=self.timeout)
        except InvalidPayload:
            raise InvalidPayload('One of the args is not a valid dictionary')
        except (requests.exceptions.RequestException,
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.URLRequired,
                requests.exceptions.TooManyRedirects,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout) as e:
            raise CouldNotSendAlert('Request errored: {}'
                                    .format(e))
        if not r.text == 'ok':
            raise CouldNotSendAlert('Invalid response: {}'
                                    .format(r.text))
