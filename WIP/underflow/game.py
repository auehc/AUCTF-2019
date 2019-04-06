from os import system, name
from random import randint
from copy import copy


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


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
    inv_string += "-------------------------------------------------"
    return inv_string


class Item:
    def __init__(self, name, value, description, hidden):
        self.name = name
        self.value = int(value)
        self.description = description
        self.instock = 1
        self.hidden = hidden

    def __str__(self):
        return self.name.ljust(15) + " " + str(self.value).ljust(10) + " " + str(self.instock) + "x"


class Shop():
    def __init__(self, filename):
        self.inventory = []
        self.wallet = 9999
        self.read_inventory_from_file(filename)
        self.yes_no = Options(["Y", "N"])

    def add_item(self, item_in):
        # populates inventory based on item_in string
        item_array = item_in.split(",")
        if len(item_array) == 4:
            ware = Item(item_array[0], item_array[1],
                        item_array[2], item_array[3])
            self.inventory.append(ware)

    def read_inventory_from_file(self, filename):
        # reads list of items from a file and sends them to add_item
        file = open(filename, "r")
        for line in file:
            self.add_item(line)
        file.close()

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
        mes = "Which item would you like to buy? Press 0 to reprint items."
        print(show_inventory(self.inventory))
        choices = Options(message=mes)
        return choices.check_input()

    def yes_no_options(self, name):
        mes = "Would you like to buy the " + name + "? "
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
                    clear()
                    if going_to_buy == '1':
                        print("The " + choice.name + " is "
                              + str(choice.value) + " credits. How much are you willing to pay?")
                        try:
                            bargin = input()
                            bargin = abs(int(bargin))
                        except ValueError:
                            print("Please only provide numbers")
                            continue

                        if bargin > user.wallet:
                            print(
                                "What do you think I am stupid? You don't have enough cash for that!")
                            print("Let's try this again...", end=' ')
                        elif bargin < choice.value:
                            print("You're gonna need more money than that!")
                            print("Let's try this again...", end=' ')
                        else:
                            clear()
                            print("Here you go!")
                            self.wallet += bargin
                            user.buy(bargin, choice)
                            choice.instock -= 1
                            not_done = False
                    else:
                        not_done = False
            else:
                print("Thats sold out! Try something else...")

        else:
            print("Invalid Option please pick another")


class User():
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
            print('You open your bag but it\'s completely empty...')
        else:
            done = False
            while not done:
                item = self.get_item()
                clear()
                inv_msg = "What would you like to do with " + item.name + "?"
                inv_choices = ['1. Check Value', '2. Inspect',
                               '3. Toss', '4. Leave Inventory']
                inv_options = Options(inv_choices, inv_msg)
                option = inv_options.check_input()
                clear()
                if option == '1':   # Get Item Value
                    print(item.value)
                elif option == '2':  # Inspect Item
                    print(item.description)
                    print("Oh! %s" % item.hidden)
                elif option == '3':  # Drop Item
                    self.drop_item(item)
                elif option == '4':  # Done
                    done = True

                if len(self.inventory) == 0:
                    break

    def drop_item(self, item):
        print("You drop the %s and the ground opens up to swallow it whole. I hope that item wasn't important or anything..." % item.name)
        self.inventory.remove(item)

    def get_item(self):
        item_msg = 'You open your bag and your items jostle around. What item would you like to select?\n'
        item_msg += show_inventory(self.inventory)
        item_choices = Options(message=item_msg)
        option = item_choices.check_input()
        option = int(option) - 1
        if option < len(self.inventory):
            return self.inventory[option]

    def check_wallet(self):
        print("You have %d credits" % self.wallet)


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
        print("You currently have: %d" % self.user_account)

    def bank_options(self, heading_to_bank):
        bank_msg = "Welcome to the bank! What would you like to do?\n"
        bank_choices = [
            "1. Withdraw",
            "2. Deposit",
            "3. Check balance",
            "4. Leave Bank",
            "5. Inspect Inventory",
            "6. Check Wallet"
        ]
        location = 'bank'
        return location_choice(bank_choices, bank_msg, heading_to_bank, location)


class Options():
    def __init__(self, choices_in=None, message=''):
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

    def check_input(self):
        print(self.message)
        self.print_choices()
        while True:
            user_input = input().lower()
            if self.type == 'number':
                try:
                    int(user_input)
                    return user_input
                except ValueError:
                    print("Please use numbers only\n")
                    continue
            elif self.options is not None and user_input not in self.options:
                clear()
                print("Please only use available choices\n")
            else:
                return user_input
            print(self.message)
            self.print_choices()

    def print_choices(self):
        for choice in self.choices:
            print(choice)


def todo():
    print("I haven't programmed that path yet...")


def shop_loc(player):
    shop = Shop("WIP/underflow/test.txt")
    heading_to_shop = True
    while(player.alive):
        user_input = shop.shop_options(heading_to_shop)
        clear()
        if user_input == '1':
            buy_choice = shop.buy_options()
            clear()
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
            print("Goodbye!")
            town_loc()
        heading_to_shop = False


def bank_loc():
    global bank
    global player
    heading_to_bank = True
    while(player.alive):
        user_input = bank.bank_options(heading_to_bank)
        clear()
        if user_input == "1":
            withdraw_msg = "How much would you like to withdraw?"
            withdraw_options = Options(message=withdraw_msg)
            withdraw = withdraw_options.check_input()
            bank.withdraw(withdraw, player)
        elif user_input == "2":
            deposit_msg = "How much would you like to deposit?"
            deposit_options = Options(message=deposit_msg)
            deposit = deposit_options.check_input()
            bank.deposit(deposit, player)
        elif user_input == "3":
            bank.check_balance()
        elif user_input == "4":
            print("Goodbye!")
            town_loc()
        elif user_input == "5":
            player.inspect_inventory()
        elif user_input == "6":
            player.check_wallet()
        heading_to_bank = False


def oasis_choice(heading_to_oasis):
    location = 'oasis'
    message = 'Wow much blue, much green...\n'
    oasis_choices = ['1. Leave']
    return location_choice(oasis_choices, message, True, location)


def oasis_loc():
    heading_to_oasis = True
    while player.alive:
        oasis_choices = oasis_choice(heading_to_oasis)
        clear()
        if oasis_choices == '1':
            desert_loc()


def desert_loc():
    global player
    heading_to_desert = True
    while player.alive:
        desert_choices = desert_choice(heading_to_desert)
        clear()
        if desert_choices == '1':    # Go to Town
            town_loc()
        elif desert_choices == '2':  # Go to Oasis
            oasis_loc()
        elif desert_choices == '3':  # Inspect Inventory
            player.inspect_inventory()
        elif desert_choices == '4':  # Check wallet
            player.check_wallet()
        heading_to_desert = False


def desert_choice(heading_to_desert):
    location = 'desert'
    desert_msg = "You see what looks to be a small town in the distance to the south and a sparkling oaisis to the north. What do you want to do?\n"

    desert_choices = ['1. Go to the Town', '2. Go to the Oasis',
                      '3. Inspect Inventory', '4. Check Wallet']
    return location_choice(desert_choices, desert_msg,
                           heading_to_desert, location)


def town_loc():
    global player
    heading_to_town = True
    while player.alive:
        user_location = town_choice(heading_to_town)
        clear()
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


def town_choice(heading_to_town):
    town_choices = ['1. Go to the Shop', '2. Go to the Desert',
                    '3. Go to the Bank', '4. Inspect Inventory', '5. Check Wallet']
    first_msg = 'You stumble upon a small town what would you like to do?\n'
    location = 'town'
    return location_choice(town_choices, first_msg,
                           heading_to_town, location)


def location_choice(choices_list, first_msg, heading_to, location, alt=''):
    if player.locations[location] == 0:
        message = first_msg
        player.locations[location] += 1
    else:
        if heading_to:
            message = 'You\'ve made your way back to the %s. What would you like to do?\n' % location
        else:
            message = alt
    choices = Options(choices_list, message)
    return choices.check_input()


def main():
    global player
    global bank
    welcome_msg = "  _____                      _      _____ _ \n\
 |  __ \                    | |    / ____| |                \n\
 | |  | | ___  ___  ___ _ __| |_  | (___ | |__   ___  _ __  \n\
 | |  | |/ _ \/ __|/ _ \ '__| __|  \___ \| '_ \ / _ \| '_ \ \n\
 | |__| |  __/\__ \  __/ |  | |_   ____) | | | | (_) | |_) |\n\
 |_____/ \___||___/\___|_|   \__| |_____/|_| |_|\___/| .__/ \n\
                                                     | |    \n\
                                                     |_|    "
    print(welcome_msg)
    print("....")
    print("....")
    print("You awaken in a desert...")
    while player.alive:
        desert_loc()


player = User()
bank = Bank()

if __name__ == "__main__":
    main()
