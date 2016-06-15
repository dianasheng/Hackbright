"""
Dictionary Code Workshop - Shopping list
There is a global dictionary that contains shopping lists by name.
We'll have a menu with options.
The core logic is in the main() function.
"""

shopping_list_by_name = {}  # key is [name] and value is [shopping list]


def add_new_shopping_list(key):
    key = key.lower()
    shopping_list = []
    if key not in shopping_list_by_name:
        shopping_list_by_name[key] = shopping_list
    else:
        print "A list with that name already exists!"


def add_item_to_shopping_list(key, item):
    item = item.lower()
    key = key.lower()

    if key in shopping_list_by_name:
        shopping_list = shopping_list_by_name[key]

        if item not in shopping_list:
            shopping_list.append(item)
            print "Here's your updated list", sorted_shopping_list(key)
        else:
            print "This item %s already exists!" % (item)
    else:
        print "There is no list with that name."


def remove_item_from_shopping_list(key, item):
    item = item.lower()
    key = key.lower()

    if key in shopping_list_by_name:
        shopping_list = shopping_list_by_name[key]
        if item in shopping_list:
            shopping_list.remove(item)
            print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list(key)
        else:
            print "%s was not on the list." % (item)
    else:
        print "There is no list with that name."


def remove_a_list(key):
    key = key.lower()

    if key in shopping_list_by_name:
        del shopping_list_by_name[key]
        print "The %s shopping list has been removed." % key
    else:
        print "There is no list with that name."


def sorted_shopping_list(key):
    key = key.lower()

    if key in shopping_list_by_name:
        shopping_list = shopping_list_by_name[key]
        shopping_list.sort()
        return shopping_list
    else:
        return None


def show_all_lists():
    print shopping_list_by_name


def menu_choice():
    print "0 - Main Menu"
    print "1 - Show all lists."
    print "2 - Show a specific list."
    print "3 - Add a new shopping list."
    print "4 - Add an item to a shopping list."
    print "5 - Remove an item from a shopping list."
    print "6 - Remove a list by nickname."
    print "7 - Type exit when you are done."

    choice = int(raw_input("Choose from the menu options."))

    return choice


def main():
    choice = menu_choice()

    while True:
        if choice == 0:
            choice = menu_choice()
        elif choice == 1:
            show_all_lists()
            choice = 0  # prompt with the main menu
        elif choice == 2:
            list_name = raw_input("Which list would you like to see?")
            print sorted_shopping_list(list_name)
            choice = 0
        elif choice == 3:
            list_name = raw_input("Enter the name for your list.")
            add_new_shopping_list(list_name)
            item = raw_input("Please enter an item.")
            while item.upper() != 'X':
                add_item_to_shopping_list(list_name, item)
                item = raw_input("Enter another item or press 'X' when done.")
            choice = 0
        elif choice == 4:
            list_name = raw_input("What's the name of the list?")
            item = raw_input("Please enter an item.")
            while item.upper() != 'X':
                add_item_to_shopping_list(list_name, item)
                item = raw_input("Enter another item or press 'X' when done.")
            choice = 0
        elif choice == 5:
            list_name = raw_input("What's the name of the list?")
            item = raw_input("Please enter an item to remove.")
            while item.upper() != 'X':
                remove_item_from_shopping_list(list_name, item)
                item = raw_input("Enter another item or press 'X' when done.")
            choice = 0
        elif choice == 6:
            list_name = raw_input("What's the name of the list?")
            remove_a_list(list_name)
            choice = 0
        elif choice == 7:
            break


if __name__ == '__main__':
    main()


