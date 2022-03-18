import os
import random
import string
from sys import platform

from termcolor import colored

settings = {
    "length": 8,
    "upper": True,
    "lower": True,
    "symbols": True,
    "numbers": True,
    "spaces": False
}

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 30


def print_password_generator_text():


    print(colored("""
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n""", color='blue'))

    print(colored("GitHub : https://github.com/Mahdifp12", 'yellow'))
    print(colored("Linkdin : https://www.linkedin.com/in/mahdi-fallaht-pishe-62b45a217/\n", 'yellow'))

def clear_screen():
    if platform in ["linux", "linux2", "darwin"]:
        os.system("clear")

    elif platform == "win32":
        os.system("cls")


def yes_or_no(option, default):

    while True:

        user_input = input(f"include {option}?"
                           f" default is {default} (y: yes, n: no, enter: default): ").lower()

        if user_input == '':
            return default

        if user_input in ['y', 'n']:

            return user_input == 'y'

        print(colored("invalid input. please try agin!", 'red'))


def get_length_from_user(option, default_length, pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):

    while True:

        user_length = input(f"Enter your password length ?"
                            f"(default is: {default_length})"
                            "(default: enter): ")

        if user_length == '':
            return default_length

        if user_length.isdigit():
            user_length = int(user_length)

            if pw_min_length <= user_length <= pw_max_length:

                return user_length

            print("Invalid input.")
            print(
                f"Password length should be between {pw_min_length} and {pw_max_length}")

        else:
            print(colored('Invalid input. you should enter a number', 'red'))

        print(colored("please try agin !", 'red'))


def get_settings_from_user(settings):

    for option, default in settings.items():
        if option != "length":
            user_choice = yes_or_no(option, default)

            settings[option] = user_choice

        else:
            user_length = get_length_from_user(option, default)

            settings[option] = user_length


def ask_if_change_settings(settings):
    while True:

        user_answer = input("do you want change default settings?"
                            "(y: yes, n: no, enter: yes): ")

        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('-'*5, colored('Change Settings', 'blue'), '-'*5, sep='')
                get_settings_from_user(settings)
            break

        else:
            print(colored("Invalid input.", 'red'))
            print(colored("Please try again.", 'red'))


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)


def get_random_numbers():
    return random.choice("123456789")


def get_random_symbols():
    return random.choice("""{)(}[]''#@!?&%$"*_="-+|/~,<>:;""")


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == "lower":
        return get_random_lower_case()
    if choice == "upper":
        return get_random_upper_case()
    if choice == "numbers":
        return get_random_numbers()
    if choice == "symbols":
        return get_random_symbols()
    if choice == "spaces":
        return " "


def password_generator():
    finally_password = ''
    password_length = settings["length"]

    choices = list(filter(lambda status: settings[status] == True,
                          ['lower', 'upper', 'symbols', 'numbers', 'spaces']))

    for i in range(password_length):
        finally_password += generate_random_char(choices)

    return finally_password


def ask_user_to_generate_another_password():
    while True:
        user_answer = input(
            'Regenerate? (y: yes, n: no, enter: yes): ').lower()
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print(colored("Invalid input.", 'red'))
            print(colored("Please try again.", 'red'))


def password_generator_loop():

    while True:
        print('-' * 30)
        print(f'Your password generated: {password_generator()}')

        if ask_user_to_generate_another_password() == False:
            break


def run():
    clear_screen()
    print_password_generator_text()
    ask_if_change_settings(settings)
    password_generator_loop()
    print(colored("Thank you choosing us.", 'green'))


run()
