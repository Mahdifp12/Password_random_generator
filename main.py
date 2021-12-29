 #? length , upper, lower, symbols, numbers, spaces

import random
import string
import pprint

settings = {
    "length": 6,
    "upper": True,
    "lower": True,
    "symbols": True,
    "numbers": True,
    "spaces": False
}


def yes_or_no(option, default):
    
    while True:

        user_input = input(f"include {option}?"
                           f" default is {default} (y: yes, n: no, enter: default): ").lower()
        
        if user_input == '':
            return default
        
        if user_input in ['y', 'n']:
        
            return user_input == 'y'
        
        
        print("invalid input. please try agin!")
        
        
def get_length_from_user(option, default_length, pw_min_length=4, pw_max_length=30):
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
            print(f"Password length should be between {pw_min_length} and {pw_max_length}")
        
        else:
            print('Invalid input. you should enter a number')
        
        print("please try agin !")
        
def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != "length":
            user_choice = yes_or_no(option, default)

            settings[option] = user_choice
        
        else:
            user_length = get_length_from_user(option, default)
            
            settings[option] = user_length

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
    elif choice == "upper":
        return get_random_upper_case()
    elif choice == "numbers":
        return get_random_numbers()
    elif choice == "symbols":
        return get_random_symbols()
    elif choice == "spaces":
        return " "


def password_generator():
    finally_password = ''
    password_length = settings["length"]
    # choices = []

    choices = list(filter(lambda status: settings[status] == True, ['lower', 'upper', 'symbols', 'numbers', 'spaces']))

    for i in range(password_length):
        finally_password += generate_random_char(choices)
        
    return finally_password


get_settings_from_user(settings)
print(password_generator())
# pprint.pprint(settings)