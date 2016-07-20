# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - Read this code and fix it.
# (Part 1): Fix any bugs and make it work!

bill = raw_input("How much was your bill?")

tip = bill * .18

total_bill = bill + tip

print "The tip is %f and the total bill is %f ." % (tip, total_bill)
