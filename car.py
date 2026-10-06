command = ""
while command != "quite":
    command = input(">").lower
    if command == "start":
        print("car started..")
    elif command == "srop":
        print("car stopped")
    elif command == "Help":
        print('''
start - start
stop - stop
quite - quite''')
