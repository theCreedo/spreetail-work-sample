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
    return

### HELP
# Give all commands and format, short description
def help():
    print(commands)

def process_command(command, args):
    return

def main():
    print("Welcome to a CLI interface to interact with a multi-value dictionary.")
    print("Please type 'HELP' to receive commands to help interact with the dictionary.")
    
    while True:
        user_input = input("Enter a command, or 'EXIT' to quit: ")
        if user_input.upper() == "EXIT":
            print("Thanks for stopping by. Till next time!")
            break
        
        args = user_input.split()
        if not args:
            print()
            continue
        
        command = args[0].upper()
        
        if command in commands:
            process_command(command, args)
        else:
            print("Invalid command. Please enter a valid command")
    return

if __name__ == "__main__":
    main()