import random
from termcolor import colored
from ascii_module.choice_ascii_string import get_random_symbols, get_random_numbers, get_random_lower_case, \
    get_random_upper_case
from settings_password_module.settings_password import print_password_generator_text, clear_screen, \
    settings
from settings_password_module.ask_settings_from_user import get_settings_from_user, ask_if_change_settings

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
