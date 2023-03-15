from random import choice
from string import ascii_lowercase, ascii_uppercase


def get_random_upper_case():
    return choice(ascii_uppercase)


def get_random_lower_case():
    return choice(ascii_lowercase)


def get_random_numbers():
    return choice("123456789")


def get_random_symbols():
    return choice("""{)(}[]''#@!?&%$"*_="-+|/~,<>:;""")
