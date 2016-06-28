"""
File I/O Lecture
Notice that we are using the uppercase constants naming convention with FILE_NAME
Notice we have to specify "global" in front of shopping list when we reassign it.
We are going to handle the "at exit" event which will trigger another function. (import atexit)
"""
import atexit

shopping_list = []
FILE_NAME = "shopping_list.txt"  # All caps denotes this variable is a constant


def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list()


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list()


def parse_input_string(input_string):
    input_string = input_string.strip()
    split_input_list = input_string.split(",")
    for item in split_input_list:
        # use the function we already wrote. Checks for dupes.
        # also strip front and end spaces
        # ignores empty string
        item = item.strip()
        if item != '':
            add_shopping_list(item)


def write_to_file():
    count = 1
    with open(FILE_NAME, mode="w") as list_file:
        list_file.write(shopping_list[0])  # writes the first item
        while count < len(shopping_list):
            list_file.write(",")  # adds a comma before the next item
            list_file.write(shopping_list[count])
            count += 1


def read_file_to_list(file_name):
    with open(file_name) as list_file:
        new_list = list_file.readlines()  # returns a list each line is an item
    return new_list


def process_file_list(file_list):
    for item in file_list:
        item = item.strip()
        split_string_list = item.split(",")
    global shopping_list  # we have to specify the global variable shopping_list
    shopping_list = split_string_list  # otherwise a new local one is created


def exit_handler():
    write_to_file()
    print 'Exiting Application'


def menu_choice():
    print "0 - Main Menu"
    print "1 - Show current list."
    print "2 - Add an item to your shopping list."
    print "3 - Remove an item from your shopping list."
    print "4 - Type exit when you are done."
    choice = int(raw_input("Choose from the menu options."))
    return choice


def main():
    file_list = read_file_to_list(FILE_NAME)
    process_file_list(file_list)
    choice = menu_choice()

    while True:
        if choice == 0:
            choice = menu_choice()
        elif choice == 1:
            print sorted_shopping_list()
            choice = 0 #  prompt with the main menu
        elif choice == 2:
            item = raw_input("Please enter an item to add OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            elif "," in item:
                parse_input_string(item)
            else:
               print add_shopping_list(item)
        elif choice == 3:
            item = raw_input("Please enter an item to remove OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            else:
                print remove_item(item)
        elif choice == 4:
            break

    atexit.register(exit_handler)


if __name__ == '__main__':
    main()


