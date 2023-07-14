from termcolor import colored
from settings_password_module.settings_password import yes_or_no, get_length_from_user

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
