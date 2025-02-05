dictionary = {}
commands = ["KEYS", "MEMBERS", "ADD", "REMOVE", "REMOVEALL", "CLEAR", "KEYEXISTS", "MEMBEREXISTS", "ALLMEMBERS", "ITEMS", "HELP"]

### KEYS
# Returns all the keys in the dictionary.
# Order is not guaranteed.
def keys():
    return

### MEMBERS
# Returns the collection of strings for the given key. 
# Return order is not guaranteed.
# Returns an error if the key does not exists.
def members(key):
    if False:
        return "ERROR, key does not exist."
    return

### ADD
# Adds a member to a collection for a given key.
# Displays an error if the member already exists for the key.
def add(key, value):
    if key_exists():
        return
    return

### REMOVE
# Removes a member from a key.
# If the last member is removed from the key, the key is removed from the dictionary.
# If the key or member does not exist, displays an error.
def remove():
    return

### REMOVEALL
# Removes all members for a key and removes the key from the dictionary.
# Returns an error if the key does not exist.
def remove_all():
    return

### CLEAR
# Removes all keys and all members from the dictionary.
def clear():
    return

### KEYEXISTS
# Returns whether a key exists or not.
def key_exists():
    return True

### MEMBEREXISTS
# Returns whether a member exists within a key.
# Returns false if the key does not exist.
def member_exists():
    return

### ALLMEMBERS
# Returns all the members in the dictionary.
# Returns nothing if there are none. Order is not guaranteed.
def all_members();
    return

### ITEMS
# Returns all keys in the dictionary and all of their members.
# Returns nothing if there are none.
# Order is not guaranteed.
def items():
    index = 1
    keys = keys()
    for key in keys:
        for member in members(key):
            print(f"{index}) {key}: {member}")
            index = index + 1

### HELP
# Give all commands
def help():
    print("Commands available: {commands}")

def invalid_arguments(command):
    print(f"Not valid # of arguments for {command}")

def verify_command(command, arg_count):
    if arg_count > 3:
        print("Too many arguments. Please use the right number of arguments")
        return False
    if command not in commands:
        print("Invalid command. Please enter a valid command")
        return False
    else:
        if command in ["MEMBERS","KEYEXISTS", "REMOVEALL"]:
            if arg_count == 2:
                return True
            else:
                invalid_arguments(command)
                return False
        elif command in ["ADD", "REMOVE", "MEMBEREXISTS"]:
            if arg_count == 3:
                return True
            else:
                invalid_arguments(command)
                return False

def process_command(command, args):
    if command == "KEYS":
        keys()
    elif command == "CLEAR":
        clear()
    elif command == "ALLMEMBERS":
        all_members()
    elif command == "ITEMS":
        items()
    elif command == "HELP":
        help()
    elif command == "MEMBERS":
        members(args[1])
    elif command == "REMOVEALL":
        remove_all(args[1])
    elif command == "KEYEXISTS":
        key_exists(args[1])
    elif command == "ADD":
        add(args[1], args[2])
    elif command == "REMOVE":
        remove(args[1], args[2])
    elif command == "MEMBEREXISTS":
        member_exists(args[1], args[2])

def main():
    print("Welcome to a CLI interface to interact with a multi-value dictionary.")
    print("Please type 'HELP' to receive commands to help interact with the dictionary.")
    
    while True:
        user_input = input("Enter a command or 'EXIT' to quit: ")
        if user_input.upper() == "EXIT" or user_input.upper() == "QUIT" or user_input.upper() == "Q":
            print("Thanks for stopping by. Till next time!")
            break
        
        args = user_input.split()
        if not args:
            print()
            continue
        
        command = args[0].upper()
        arg_count = len(args)
        if verify_command(command, arg_count):
            process_command(command, args)
    return

if __name__ == "__main__":
    main()