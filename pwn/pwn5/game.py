#!/usr/bin/env python3

from os import system, name
from random import randint
from copy import copy
from time import sleep
import sys


class Item:
    def __init__(self, name, value, description, hidden):
        self.name = name
        self.value = int(value)
        self.description = description
        self.instock = 1
        self.hidden = hidden

    def __str__(self):
        return self.name.ljust(15) + " " + str(self.value).ljust(10) + " " + str(self.instock) + "x"


class Shop:
    def __init__(self):
        self.inventory = []
        self.wallet = 9999
        self.create_invenotry()
        self.yes_no = Options(["Y", "N"])

    def add_item(self, item_in):
        # populates inventory based on item_in string
        item_array = item_in.split(",")
        if len(item_array) == 4:
            ware = Item(item_array[0], item_array[1],
                        item_array[2], item_array[3])
            self.inventory.append(ware)

    def create_invenotry(self):
        # reads list of items from a file and sends them to add_item
        string_list = ["holy grail, 50, magical object, you now live forever",
                       "flag,9999,very special,aubie{logical_flaws}",
                       "tiger,2,bites,you've lost 2 fingers",
                       "DL-44, 1977, favorite weapon of nerf hearders, you now feel the urge to do some smuggling"]
        for line in string_list:
            self.add_item(line)

    def get_item(self, ware):
        # returns item from inventory if ware matches it
        for inv in self.inventory:
            if ware.lower() == inv.name.lower():
                return inv

    def welcome(self):
        # prints out random greeting from grettings list
        greetings = ['Welcome to my Shop!\n']
        random_int = randint(0, len(greetings) - 1)
        return greetings[random_int]

    def shop_options(self, heading_to_shop):
        shop_choices = [
            "1. Buy Item",
            "2. See Shop Inventory",
            "3. Check Wallet",
            "4. Inspect Inventory",
            "5. Leave Shop", ]
        message = self.welcome()
        location = 'shop'
        return location_choice(shop_choices, message, heading_to_shop, location)

    def buy_options(self):
        mes = "Which item would you like to buy? Press 0 to reprint items.\n"
        print(show_inventory(self.inventory))
        choices = Options(message=mes)
        return choices.check_input()

    def yes_no_options(self, name):
        mes = "Would you like to buy the " + name + "?\n"
        yes_no = ["1. Yes",
                  "2. No"]
        choices = Options(yes_no, mes)
        return choices.check_input()

    def sell_item(self, option, user):
        not_done = True
        option = int(option) - 1
        if option < len(self.inventory):
            choice = self.inventory[option]
            if choice.instock != 0:
                while not_done:
                    going_to_buy = self.yes_no_options(choice.name)

                    if going_to_buy == '1':
                        print_slowly("The " + choice.name + " is " +
                                     str(choice.value) + " credits. How much are you willing to pay?\n")
                        try:
                            bargin = input()
                            bargin = abs(int(bargin))
                        except ValueError:
                            print_slowly("Please only provide numbers")
                            continue

                        if bargin > user.wallet:
                            print_slowly(
                                "What do you think I am stupid? You don't have enough cash for that!")
                            print_slowly("Let's try this again...")
                        elif bargin < choice.value:
                            print_slowly(
                                "You're gonna need more money than that!")
                            print_slowly("Let's try this again...")
                        else:

                            print_slowly("Here you go!\n")
                            self.wallet += bargin
                            user.buy(bargin, choice)
                            choice.instock -= 1
                            not_done = False
                    else:
                        not_done = False
            else:
                print_slowly("That's sold out! Try something else...\n")

        else:
            print_slowly("Invalid Option please pick another.\n")


class User:
    def __init__(self):
        self.wallet = 250
        self.inventory = []
        self.alive = True
        self.locations = {
            'desert': 0,
            'oasis': 0,
            'town': 0,
            'shop': 0,
            'tavern': 0,
            'bank': 0
        }

    def buy(self, price, item):
        co_item = copy(item)
        self.wallet -= price
        self.inventory.append(co_item)

    def inspect_inventory(self):
        if len(self.inventory) == 0:
            print_slowly('You open your bag but it\'s completely empty...\n')
        else:
            done = False
            while not done:
                item = self.get_item()

                if item == None:  # Done
                    return
                if item == 0:
                    print_slowly("Please only use available choices\n")
                    continue
                inv_msg = "What would you like to do with " + item.name + "?\n"
                inv_choices = ['1. Check Value', '2. Inspect',
                               '3. Toss', '4. Leave Inventory']
                inv_options = Options(inv_choices, inv_msg)
                option = inv_options.check_input()

                if option == '1':   # Get Item Value
                    print_slowly("The %s is %d credits" %
                                 (item.name, item.value))
                elif option == '2':  # Inspect Item
                    print_slowly(item.description)
                    print_slowly("Oh! %s" % item.hidden)
                elif option == '3':  # Drop Item
                    self.drop_item(item)
                elif option == '4':  # Done
                    done = True
                if len(self.inventory) == 0:
                    break

    def drop_item(self, item):
        print_slowly(
            "You drop the %s and the ground opens up to swallow it whole. I hope that item wasn't important or anything..." % item.name)
        self.inventory.remove(item)

    def get_item(self):
        item_msg = 'You open your bag and your items jostle around. What item would you like to select? Press 0 to leave inventory.\n'
        # item_msg += show_inventory(self.inventory)
        item_choices = Options(message=item_msg)
        print(show_inventory(self.inventory))
        option = item_choices.check_input()
        if option == '0':
            return None
        else:
            option = int(option) - 1
            if option < len(self.inventory):
                return self.inventory[option]
        return 0

    def check_wallet(self):
        print_slowly("You have %d credits\n" % self.wallet)


class Bank:
    def __init__(self):
        self.user_account = 500

    def deposit(self, value, player):
        value = int(value)
        if value <= player.wallet:
            self.user_account += value
            player.wallet -= value

    def withdraw(self, value, player):
        value = int(value)
        if value <= self.user_account:
            player.wallet += value
            self.user_account -= value

    def check_balance(self):
        print_slowly("You currently have: %d" % self.user_account)

    def bank_options(self, heading_to_bank):
        bank_msg = "Welcome to the bank! What would you like to do?\n"
        bank_choices = [
            "1. Withdraw",
            "2. Deposit",
            "3. Check balance",
            "4. Inspect Inventory",
            "5. Check Wallet",
            "6. Leave Bank",
        ]
        location = 'bank'
        return location_choice(bank_choices, bank_msg, heading_to_bank, location)


class Options:
    def __init__(self, choices_in=None, message='\n'):
        self.message = message
        if choices_in == None:
            self.choices = []
            self.options = None
            self.type = 'number'
            return
        else:
            self.choices = []
            self.options = []
            self.type = 'strings'

        for choice in choices_in:
            self.choices.append(choice)  # grab full choice

            choice = choice[0][0]   # get only the beggining of the choice
            self.options.append(choice)
        if choices_in != None:
            self.options.append("*")

    def check_input(self):
        print_slowly(self.message)
        self.print_choices()
        while True:
            user_input = input().lower()
            if user_input == "*":
                exit_game()
            if self.type == 'number':
                try:
                    int(user_input)
                    return user_input
                except ValueError:
                    print_slowly("Please use numbers only\n")
                    continue
            elif self.options is not None and user_input not in self.options:

                print_slowly("Please only use available choices\n")
            else:
                return user_input
            print_slowly(self.message)
            self.print_choices()

    def print_choices(self):
        for choice in self.choices:
            print(choice)
        if self.choices != []:
            print("*. Exit Game")
            print()


def show_inventory(inventory):
    # prints current inventory to the screen
    inv_string = "--------------------- Items ---------------------\n"
    inv_string += "-- Name ---------- Value ---- Stock -------------\n"
    i = 1
    for item in inventory:
        counter = str(i) + "."
        inv_string += counter.ljust(3)
        inv_string += item.__str__()
        inv_string += "\n"
        i += 1
    inv_string += "-------------------------------------------------\n"
    return inv_string

################################# Location Functions ################################


def desert_loc():
    # Handles user input for desert location
    global player
    heading_to_desert = True
    while player.alive:
        desert_choices = desert_choice(heading_to_desert)

        if desert_choices == '1':    # Go to Town
            town_loc()
        elif desert_choices == '2':  # Go to Oasis
            oasis_loc()
        elif desert_choices == '3':  # Inspect Inventory
            player.inspect_inventory()
        elif desert_choices == '4':  # Check wallet
            player.check_wallet()
        heading_to_desert = False


def oasis_loc():
    # Handles uer input for oasis
    heading_to_oasis = True
    while player.alive:
        oasis_choices = oasis_choice(heading_to_oasis)

        if oasis_choices == '1':
            desert_loc()


def town_loc():
    # Handles user input for town
    global player
    heading_to_town = True
    while player.alive:
        user_location = town_choice(heading_to_town)

        if user_location == '1':    # Go to shop
            shop_loc(player)
        elif user_location == '2':  # Go to desert
            desert_loc()
        elif user_location == '3':  # Go to bank
            bank_loc()
        elif user_location == '4':  # Inspect inventory
            player.inspect_inventory()
        elif user_location == '5':  # Check wallet
            player.check_wallet()
        heading_to_town = False


def shop_loc(player):
    # Handles user input for shop
    shop = Shop()
    heading_to_shop = True
    while(player.alive):
        user_input = shop.shop_options(heading_to_shop)

        if user_input == '1':
            buy_choice = shop.buy_options()
            if buy_choice == '0':
                print(show_inventory(shop.inventory))
            else:
                shop.sell_item(buy_choice, player)
        elif user_input == '2':  # Show shop inventory
            print(show_inventory(shop.inventory))
        elif user_input == '3':  # Check wallet
            player.check_wallet()
        elif user_input == '4':  # Check player inventory
            player.inspect_inventory()
        elif user_input == '5':  # Leave shop
            town_loc()
        heading_to_shop = False


def bank_loc():
    # Handles user input for bank
    global bank
    global player
    heading_to_bank = True
    while(player.alive):
        user_input = bank.bank_options(heading_to_bank)

        if user_input == "1":
            withdraw_msg = "How much would you like to withdraw?\n"
            withdraw_options = Options(message=withdraw_msg)
            withdraw = withdraw_options.check_input()
            bank.withdraw(withdraw, player)
        elif user_input == "2":
            deposit_msg = "How much would you like to deposit?\n"
            deposit_options = Options(message=deposit_msg)
            deposit = deposit_options.check_input()
            bank.deposit(deposit, player)
        elif user_input == "3":
            bank.check_balance()
        elif user_input == "4":
            player.inspect_inventory()
        elif user_input == "5":
            player.check_wallet()
        elif user_input == "6":
            town_loc()
        heading_to_bank = False


def town_choice(heading_to_town):
    # Choices for town, will call location_choice
    town_choices = ['1. Go to the Shop', '2. Go to the Desert',
                    '3. Go to the Bank', '4. Inspect Inventory', '5. Check Wallet']
    first_msg = 'You stumble upon a small town that contains a shop and a bank what would you like to do?\n'
    location = 'town'
    return location_choice(town_choices, first_msg,
                           heading_to_town, location)


def desert_choice(heading_to_desert):
    location = 'desert'
    desert_msg = "You see what looks to be a small town in the distance to the south and a sparkling oasis to the north. What do you want to do?\n"

    desert_choices = ['1. Go to the Town', '2. Go to the Oasis',
                      '3. Inspect Inventory', '4. Check Wallet']
    return location_choice(desert_choices, desert_msg,
                           heading_to_desert, location)


def oasis_choice(heading_to_oasis):
    location = 'oasis'
    message = 'Wow much blue, much green...\n'
    oasis_choices = ['1. Leave']
    return location_choice(oasis_choices, message, True, location)


def location_choice(choices_list, first_msg, heading_to, location):
    # Print out choices for passed location, if heading to the location will print out a different message
    if player.locations[location] == 0:
        message = first_msg
        player.locations[location] += 1
    else:
        if heading_to:
            message = 'You\'ve made your way back to the %s. What would you like to do?\n' % location
        else:
            message = "You are still in the %s. What would you like to do?\n" % location
    choices = Options(choices_list, message)
    return choices.check_input()

#####################################################################################


################################# Utility Functions #################################


def print_slowly(string, speed=0.025):
    # Prints passed string slowly, default speed 1 characters per 0.05 seconds
    for char in string:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()


def exit_game():
    print("Goodbye~")
    sys.exit(1)


def todo():
    print_slowly("I haven't programmed that path yet...")


#####################################################################################


def boot():
    # Print boot up messages
    welcome_msg = "  _____                      _      _____ _ \n\
 |  __ \                    | |    / ____| |                \n\
 | |  | | ___  ___  ___ _ __| |_  | (___ | |__   ___  _ __  \n\
 | |  | |/ _ \/ __|/ _ \ '__| __|  \___ \| '_ \ / _ \| '_ \ \n\
 | |__| |  __/\__ \  __/ |  | |_   ____) | | | | (_) | |_) |\n\
 |_____/ \___||___/\___|_|   \__| |_____/|_| |_|\___/| .__/ \n\
                                                     | |    \n\
                                                     |_|    "
    print(welcome_msg)
    print("Loading", end='')
    print_slowly(".....", 0.5)

    print_slowly("You awaken in a desert...")


def main():
    global player
    global bank
    boot()
    while player.alive:
        desert_loc()


player = User()
bank = Bank()

if __name__ == "__main__":
    main()
