"""
Core curate exceptions
"""


class CurateAjaxError(Exception):
    """
    Exception raised by the curate package from views.
    """

    def __init__(self, message):
        self.message = message


class CurateValidationError(Exception):
    """
    Validation Exception raised by the curate package.
    """

    def __init__(self, message):
        self.message = message
