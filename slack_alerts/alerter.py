class Alerter:
    """ Alert manager

    Contains the configuration for a given slack channel:
    - api_key
    - channel
    """

    def __init__(self, url: str, channel: str,
                 username: str = __name__, icon_emoji: str = None):
        self.url = url
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji

    def critical():
        pass

    def warning():
        pass

    def info():
        pass
