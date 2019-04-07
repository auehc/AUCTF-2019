from time import sleep
print(
    "Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32")
print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")

banned = [
    "import",
    "exec",
    "eval",
    "pickle",
    "os",
    "subprocess",
    "help",
    "input",
    "banned",
    "lol",
    "sys",
    "access",
]

targets = __builtins__.__dict__

count = 0
while 1:
    print(">>>", end=' ')
    data = input()

    for no in banned:
        if no.lower() in data.lower():
            sleep(1)
            if count == 2:
                print("access: PERMISSION DENIED", end='')
                sleep(.5)
                print("....and...")
                sleep(.8)
                while True:
                    sleep(.3)
                    print("YOU DIDN'T SAY THE MAGIC WORD!")
            else:
                print("access: PERMISSION DENIED")
            count += 1
            break
    else:
        try:
            exec(data)
        except:
            print("Sorry to say that's not a valid command")
