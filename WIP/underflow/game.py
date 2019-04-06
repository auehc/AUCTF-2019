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
            ware = Item(item_array[0], item_array[1], item_array[2], item_array[3])
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
        greetings = ['Welcome to my Shop!']
        random_int = randint(0, len(greetings) - 1)
        print(greetings[random_int])

    def shop_options(self):
        shop_op = [
            "1. Buy Item",
            "2. Check Wallet",
            "3. Leave Shop"]
        inv = show_inventory(self.inventory)
        choices = Options(shop_op, inv)
        return choices.check_input()

    def buy_options(self):
        mes = "Which item would you like to buy? Press 0 to reprint items."
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
                    if going_to_buy == '1':
                        # while not_done:

                        print("The " + choice.name + " is $" +
                              str(choice.value) + ". How much are you willing to pay?")
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
            'desert':0,
            'oasis':0,
            'town':0,
            'shop':0,
            'tavern':0
        }

    def buy(self, price, item):
        co_item = copy(item)
        self.wallet -= price
        self.inventory.append(co_item) 
                                      
    def inspect_inventory(self):
        if len(self.inventory) == 0:
            print('You open your bag but its completely empty...')
        else:
            done = False
            while not done:
                item = self.get_item()
                inv_msg = "What would you like to do with " + item.name + "?"
                inv_choices = ['1. Check Value', '2. Inspect', '3. Toss', '4. Leave Inventory']
                inv_options = Options(inv_choices, inv_msg)
                option = inv_options.check_input()
                if option == '1':
                    print(item.value)
                elif option == '2':
                    print(item.description)
                    print("Oh! %s" % item.hidden)
                elif option == '3':
                    todo() # TODO
                elif option == '4':
                    done = True

    def get_item(self):
        item_msg = 'You open your bag and your items jostle around. What would you like to inspect?\n'
        item_msg += show_inventory(self.inventory)
        item_choices = Options(message = item_msg)
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
                    print("Please use numbers only")
                    self.print_choices()
                    continue
            elif self.options is not None and user_input not in self.options:
                print("Please only use available choices")
                self.print_choices()
            else:
                return user_input

    def print_choices(self):
        for choice in self.choices:
            print(choice)

def shop_enter(player):
    shop = Shop("WIP/underflow/test.txt")
    shop.welcome()
    done = False
    while(not done):
        user_input = shop.shop_options()
        if user_input == '1':
            buy_choice = shop.buy_options()
            if buy_choice == '0':
                print(show_inventory(shop.inventory))
            else:
                shop.sell_item(buy_choice, player)
        elif user_input == '2':
           player.check_wallet()
        elif user_input == '3':
            print("Goodbye!")
            done = True

def todo():
    print("I haven't programmed that path yet...")

def bank_loc():
    global bank
    global player
    done = False
    bank_msg = "Welcome to the bank! What would you like to do?"
    bank_choices = [
        "1. Withdraw",
        "2. Deposit",
        "3. Check balance",
        "4. Leave Bank",
        "5. Inspect Inventory",
        "6. Check Wallet"
    ]
    bank_options = Options(bank_choices, bank_msg)
    while(not done):
        user_input = bank_options.check_input()
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
            done = True
            print("Goodbye!")
        elif user_input == "5":
            player.inspect_inventory()
        elif user_input == "6":
            player.check_wallet()
def desert():
    global player
    if player.locations['desert'] == 0:
        desert_msg = "You see what looks to be a small town in the distance to the south and a sparkling oaisis to the north. Where do you want to go?"
        player.locations['desert'] += 1
    else:
        desert_msg = 'You\'ve made your way back to the desert. Where would you like to head?'
    desert_choices = ['1. Town', '2. Oasis', '3. Inspect Inventory', '4. Check Wallet']
    desert_options = Options(desert_choices, desert_msg)
    desert_choice = desert_options.check_input()
    if desert_choice == '1':
        town()
    elif desert_choice == '2':
        todo() # TODO
    elif desert_choice == '3':
        player.inspect_inventory()
    elif desert_choice == '4':
        player.check_wallet()
        
def town():
    global player 
    while player.alive:
        town_choices = ['1. Shop','2. To the Desert','3. Bank', '4. Inspect Inventory', '5. Check Wallet']
        if player.locations['town'] == 0:
            town_msg = 'You stumble upon a small town where would you like to head?'
            player.locations['town'] += 1
        else:
            town_msg = 'You are in the town. Where would you like to head?'
        locations = Options(town_choices, town_msg)
        user_location = locations.check_input()
        if user_location == '1':
            shop_enter(player)
        elif user_location == '2':
            desert()
        elif user_location == '3':
            bank_loc() # TODO
        elif user_location == '4':
            player.inspect_inventory()
        elif user_location == '5':
            player.check_wallet()

def main():
    global player
    global bank
    print("Welcome to the game!")
    print("....")
    print("....")
    print("You awaken in a desert...")
    while player.alive:
        desert()



player = User()
bank = Bank()

main()