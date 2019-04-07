print("Python 3.6.7 (default, Oct 22 2018, 11: 32: 17")
print("[GCC 8.2.0] on linux")
print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")


while 1:
    print(">>>", end=' ')
    data = input()
    try:
        exec(data)
    except:
        print("Sorry to say that's not a valid command")
