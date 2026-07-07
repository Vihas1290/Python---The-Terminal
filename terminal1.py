command = input("Command: ")

run = True

while run: 
    if command == "exit":
        run = False
    elif command.startswith("echo"):
        print(command[4:])
        command = input("Command: ")
    elif command == "cd":
        print("\'C:/Users/Dummy\' is your current directory")
        command = input("Command: ")
    elif command == "help":
        print("Options: echo \'\', help, cd, exit")
        print("echo \'\': Print whatever comes after echo")
        print("help: Displays this menu")
        print("cd: Shows current directory")
        command = input("Command: ")
    elif command == "add":
        x = int(input("No.1: "))
        y = int(input("No.2: "))
        print(x + y)
        command = input("Command: ")
    elif command == "sub":
        x = int(input("No.1: "))
        y = int(input("No.2: "))
        print(x - y)
        command = input("Command: ")
    elif command == "mul":
        x = int(input("No.1: "))
        y = int(input("No.2: "))
        print(x * y)
        command = input("Command: ")
    elif command == "div":
        x = int(input("No.1: "))
        y = int(input("No.2: "))
        print(x / y)
        command = input("Command: ")

