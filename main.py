import random
from termcolor import colored
from ascii_module.choice_ascii_string import get_random_symbols, get_random_numbers, get_random_lower_case, \
    get_random_upper_case
from settings_password_module.settings_password import print_password_generator_text, clear_screen, \
    yes_or_no, get_length_from_user, settings

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
                print('-' * 5, colored('Change Settings', 'blue'), '-' * 5, sep='')
                get_settings_from_user(settings)
            break

        else:
            print(colored("Invalid input.", 'red'))
            print(colored("Please try again.", 'red'))


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

    choices = list(filter(lambda status: settings[status] is True,
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

        if not ask_user_to_generate_another_password():
            break


if __name__ == "__main__":
    clear_screen()
    print_password_generator_text()
    ask_if_change_settings(settings)
    password_generator_loop()
    print(colored("Thank you choosing us.", 'green'))
