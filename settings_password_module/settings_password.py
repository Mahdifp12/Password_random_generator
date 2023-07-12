import os
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
    os.system("clear") if platform in ["linux", "linux2", "darwin"] else os.system("cls")


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
