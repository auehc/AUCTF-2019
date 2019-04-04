from os import system, name
from random import randint


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
            "2. Inspect Item",
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
                            user.inventory.append(choice)   ## TODO need to make copy of choice, right now its using the same choice from 
                            not_done = False                ## shops inventory therefore when you subtract instock from it it takes it away
                    else:                                   ## from the user
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

    def buy(self, price, item):
        self.wallet -= price
        self.inventory.append(item)

    def inspect_inventory(self):
        if len(self.inventory) == 0:
            print('You open your bag but its completely empty...')
        else:
            item = self.get_item()
            inv_msg = "What would you like to do with " + item.name + "?"
            inv_choices = ['1. Check Value', '2. Inspect', '3. Toss']
            inv_options = Options(inv_choices, inv_msg)
            option = inv_options.check_input()
            if option == '1':
                print(item.value)
            elif option == '2':
                print(item.description)
                print("Oh! %s" % item.hidden)

    def get_item(self):
        item_msg = 'You open your bag and your items jostle around. What would you like to inspect?\n'
        item_msg += show_inventory(self.inventory)
        item_choices = Options(message = item_msg)
        option = item_choices.check_input()
        option = int(option) - 1
        if option < len(self.inventory):
            return self.inventory[option]
    

    

 


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
            print("TODO")
        elif user_input == '3':
            print("Goodbye!")
            done = True


def desert(player):
    desert_msg = "You see what looks to be a small town in the distance to the south and a sparkling oaisis to the north. Where do you want to go?"
    desert_choices = ['1. Town', '2. Oasis']
    desert_options = Options(desert_choices, desert_msg)
    desert_choice = desert_options.check_input()
    if desert_choice == '1':
        town(player)
    elif desert_choice == '2':
        None # TODO
def town(player):
    while player.alive:
        town_choices = ['1. Shop','2. To the Desert','3. Tavern', '4. Inspect Inventory']
        town_msg = 'You stumble upon a small town where would you like to head?'
        locations = Options(town_choices, town_msg)
        user_location = locations.check_input()
        if user_location == '1':
            shop_enter(player)
        elif user_location == '2':
            None # TODO
        elif user_location == '3':
            desert(player)
        elif user_location == '4':
            player.inspect_inventory()


def main():
    player = User()
    while player.alive:
        desert(player)

main()