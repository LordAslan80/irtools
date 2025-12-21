from .tools.tel import Tel
from .tools.digits import Digits
from .tools.national_code import NationalCode


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


def digits(value, option="ef"):
    """convert english digits to farsi digits and reverse

    Args:
        value (str): your input string
        option (str): only accepts ef, fe
            ef (default) -> convert english digits to farsi digits
            fe -> convert farsi digits to english digits

    Returns:
        string: return input string with replaced digits
        False: if any errors occur
    """
    return Digits(value, option).run


def national_code(value, option="v"):
    """validate national code

    Args:
        value (str): person input national code
        option (str, optional): only accepts v, c, cc, cp
            v (default) -> validate national code
            c -> return born city and province
            cc -> return born city
            cp -> return born province

    Returns:
        False: if any error occurs or validation fails or city doesn't exist
        True: if national code is valid
        string: city name
    """
    return NationalCode(value, option).run
