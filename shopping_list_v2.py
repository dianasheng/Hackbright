def add_shopping_list(item, shopping_list):
    if(item not in shopping_list):
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list(shopping_list)
    else: print "This item %s already exists!" % (item)

def sorted_shopping_list(shopping_list):
    shopping_list.sort()
    return shopping_list

def num_items_in_shopping_list(shopping_list):
    return len(shopping_list)

def remove_item(item, shopping_list):
    if(item in shopping_list):
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list(shopping_list)
    else: print "%s was not on the list." % (item)

def replace_item(old_item, new_item, shopping_list):
    if(old_item in shopping_list):
        item_index = shopping_list.index(old_item)
        print "%s has replaced %s in the list." % (new_item, old_item)
    else: print "%s is not in the list." % (old_item)

#make use of your functions
#create a shopping list
my_shopping_list = []
#1 - add 4 times to your shopping list
add_shopping_list("apple", my_shopping_list)
add_shopping_list("steak", my_shopping_list)
add_shopping_list("beef", my_shopping_list)
add_shopping_list("mustard", my_shopping_list)
#2 - Add an item that is already in the list. what happens?
add_shopping_list("apple", my_shopping_list)
#3 - Remove an item on your list
remove_item("apple", my_shopping_list)
#4 - Remove an item that is not in the list. what happens?
remove_item("chicken", my_shopping_list)
#5 - Print the number of items in your shopping list.
print "There are %i items on the shopping list" % (num_items_in_shopping_list(my_shopping_list))
#6 - you've changed your mind on one of your items. you want to substitute it with something else.
replace_item("mustard", "ketchup", my_shopping_list)
#7 print shopping list
print sorted_shopping_list(my_shopping_list)
