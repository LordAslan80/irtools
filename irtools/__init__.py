from .tools.tel import Tel
from .tools.utils import Numbers


def tel(value, option="v"):
    """convert or validate phone number

    Args:
        value (str): value only can be contains of digits and + character
        option (str): only accepts v, v0, v9, v+, c0, c9, c+
            v (default) -> validate tel if it starts with 09xxx or 98xxx or +98xxx
            v0 -> validate tel if starts with 09xxx
            v9 -> validate tel if starts with 989xxx
            v+ -> validate tel if starts with +989xxx
            c0 -> first validate then convert to 09xxx
            c9 -> first validate then convert to 989xxx
            c+ -> first validate then convert to +989xxx

    Returns:
        boolean: if use v, v0, v9, v+
        string: if use c0, c9, c+
        False: if any error occur or validation fails
    """
    return Tel(value, option).run


def num(value, option="ef"):
    """convert english digits to farsi digits and reverse

    Args:
        value (str): your input string
        option (str): only accepts ef, fe
            ef (default) -> convert english digits to farsi digits
            fe -> convert farsi digits to english digits

    Returns:
        string: return input string with replaced digits
    """
    return Numbers(value, option).run
