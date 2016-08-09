"""
Loops Lecture - Shopping list
This project is a shopping list app.
We have a global list that will be our shopping list.
We'll have a menu with options.
The program will keep running until it is closed.
The core logic is in the main() function.
"""
shopping_list = []


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


def menu_choice():
    print "0 - Main Menu"
    print "1 - Show current list."
    print "2 - Add an item to your shopping list."
    print "3 - Remove an item from your shopping list."
    print "4 - Exit the program."
    choice = int(raw_input("Choose from the menu options."))
    return choice


def main():
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


if __name__ == '__main__':
    main()


