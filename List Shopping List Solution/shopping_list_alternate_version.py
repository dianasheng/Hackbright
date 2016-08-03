"""
Lists Lecture Exercise.
This project is a shopping list app.
This version has a local shopping list instead of a global one.
The functions will take an item and a list.
Make sure your code deals with upper and lower case.
"""


def add_shopping_list(item, shopping_list):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list(shopping_list)


def sorted_shopping_list(shopping_list):
    shopping_list.sort()
    return shopping_list


def remove_item(item, shopping_list):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list(shopping_list)


def main():

    # TEST FUNCTIONS
    # create a list
    shopping_list = []
    # 1 - add 4 times to your shopping list
    print add_shopping_list("apple", shopping_list)
    print add_shopping_list("steak", shopping_list)
    print add_shopping_list("beef", shopping_list)
    print add_shopping_list("mustard", shopping_list)

    # 2 - Add an item that is already in the list. what happens?
    print add_shopping_list("apple", shopping_list)

    # 3 - Remove an item on your list
    print remove_item("apple", shopping_list)

    # 4 - Remove an item that is not in the list. what happens?
    print remove_item("chicken", shopping_list)


if __name__ == "__main__":
    main()
