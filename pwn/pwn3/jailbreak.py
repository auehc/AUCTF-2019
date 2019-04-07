from time import sleep
print(
    "Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32")
print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")


targets = __builtins__.__dict__

count = 0
while 1:
    print(">>>", end=' ')
    data = input()
    try:
        exec(data)
    except:
        print("Sorry to say that's not a valid command")
