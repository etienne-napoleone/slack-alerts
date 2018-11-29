class NoSuchAlerter(Exception):
    """
    Raised when trying to get a non existing alerter.
    """


class CouldNotSendAlert(Exception):
    """
    Raised when sending the alert failed.
    """
