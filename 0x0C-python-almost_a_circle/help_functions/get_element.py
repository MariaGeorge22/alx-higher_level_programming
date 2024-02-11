"""
Helper Functions
"""


def get_element(args, i, default_value=None):
    """
    safe getter from args
    """
    try:
        return args[i]
    except IndexError:
        return default_value