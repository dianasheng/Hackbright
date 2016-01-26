# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - fix this code :D
# (Part 1): Instead of using the hard coded ".18",
# Ask the user to input the percentage of tip they want to give. 
# Save the input to a variable. 
# Use the variable to calculate the tip.
# (Part 2): Fix any bugs and make it work!

bill = raw_input("How much was your bill?")

tip = bill * .18

total_bill = bill + tip

print "The tip is %f and the total bill is %f ." % (tip, total_bill)
