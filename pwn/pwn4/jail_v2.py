from copy import copy


print("Python 3.6.7 (default, Oct 22 2018, 11: 32: 17")
print("[GCC 8.2.0] on linux")
print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")

banned = [
    "import",
    "exec",
    "eval",
    "pickle",
    "os",
    "subprocess",
    "aubie",
    "help"
    "input",
    "banned",
    "jordan",
    "demarcus",
    "sys",
    "from"
]


def test():
    print("aubie{wait_we're_smarter-than_this}")


while True:
    print(">>>", end=' ')
    data = input()

    for no in banned:
        if no.lower() in data.lower():
            print("Sorry can't let you do that...")
            break
    else:  # this means nobreak
        try:
            exec(data)
        except:
            print("Sorry to say that's not a valid command")
