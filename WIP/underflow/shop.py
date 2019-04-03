from os import system, name
from random import randint


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = int(value)
        self.description = description
        self.instock = 1

    def __str__(self):
        return self.name.ljust(15) + " " + str(self.value).ljust(10) + " " + str(self.instock) + "x"


class Shop():
    def __init__(self, filename):
        self.inventory = []
        self.wallet = 9999
        self.read_inventory_from_file(filename)
        self.yes_no = Options(["Y", "N"])

    def show_inventory(self):
        # prints current inventory to the screen
        inv_string = "--------------------- Items ---------------------\n"
        i = 1
        for item in self.inventory:
            counter = str(i) + "."
            inv_string += counter.ljust(3)
            inv_string += item.__str__()
            inv_string += "\n"
            i += 1
        inv_string += "-------------------------------------------------"
        return inv_string

    def add_item(self, item_in):
        # populates inventory based on item_in string
        item_array = item_in.split(",")
        if len(item_array) == 3:
            ware = Item(item_array[0], item_array[1], item_array[2])
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
            "2. Inspect Item",
            "3. Leave Shop"]
        inv = self.show_inventory()
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
                            bargin = int(bargin)
                        except ValueError:
                            print("Please only provide numbers")
                            continue

                        if int(bargin) > user.wallet:
                            print(
                                "What do you think I am stupid? You don't have enough cash for that!")
                            print("Let's try this again...", end=' ')
                        elif abs(bargin) < choice.value:
                            print("You're gonna need more money than that!")
                            print("Let's try this again...", end=' ')
                        else:
                            print("Here you go!")
                            self.wallet += bargin
                            choice.instock -= 1
                            user.inventory.append(choice)
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

    def buy(self, price, item):
        self.wallet -= price
        self.inventory.append(item)

    def inspect_inventory(self):
        # TODO
        None


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


player = User()
shop = Shop("WIP/underflow/test.txt")
shop.welcome()


done = False
while(not done):
    user_input = shop.shop_options()
    if user_input == '1':
        buy_choice = shop.buy_options()
        if buy_choice == '0':
            print(shop.show_inventory())
        else:
            shop.sell_item(buy_choice, player)
    elif user_input == '2':
        print("TODO")
    elif user_input == '3':
        print("Goodbye!")
        done = True
