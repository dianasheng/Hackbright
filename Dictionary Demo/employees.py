'''
Learn how dictionaries work
'''

# creates an empty dictionary
Employee = {}

# Here are ways to add [key:value] pairs
Employee['name'] = 'Sarah'
Employee['age'] = 26
Employee['height'] =  61#raw_input('Please Enter your height: ')
Employee['age'] = 27 #What happens to 'age' with this line of code?

# Check if the key 'name' exists, if so access the value
if 'name' in Employee:
    print "Key: %s Value: %s" % ("name", Employee['name'])
else: print "Key: %s does not exist." % ("name")

# Check if the key 27 exists, if so access the value
if 27 in Employee:
    print "Key: %s Value: %s" % (27, Employee[27])
else: print "Key: %s does not exist." % (27)

# iterate over the keys in Employee
for key1 in Employee:
    print "%s is a key in Employee." % (key1)

# View the keys in Employee
print Employee.keys()
print Employee.items()

#Iterate with key:value pairs in Employee
for key,value in Employee.items():
    print "These are key:value pairs: %s , %s" % (key,value)

#view the key:value pairs
print Employee
