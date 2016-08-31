from operator import attrgetter


# class definition for a Contact
class Contact(object):
    # initialize an instance of the object Contact
    def __init__(self, first_name, last_name, mobile_phone = "", work_phone = "", email = "", twitter_handle=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.twitter_handle = twitter_handle

    def send_tweet(self, message_string):
        if self.twitter_handle != "":
            print "To: %s - %s" % (self.twitter_handle, message_string)
        else: print "No twitter handle set."

    def send_text(self, phone_number, message_string):
        print "To: %s - %s" % (phone_number, message_string)

    def send_email(self, message_string):
        if self.email != "":
            print "Sending message: %s to %s." % (message_string, self.email)
        else: print "No email address."


# TESTING THE CONTACT CLASS
# Create two contacts and add them to a list.
# Print out the contacts to see that it worked.

def main():
    contacts_list = []


    contact_diana = Contact("Diana", "Banana")
    contact_diana.mobile_phone = "415-555-5000"
    contacts_list.append(contact_diana)

    contact_james = Contact("James", "Frank")
    contact_james.email = "james@frank.com"
    contacts_list.append(contact_james)

    contact_amy = Contact("Amy", "Banana")
    contact_amy.mobile_phone = "415-555-5555"
    contacts_list.append(contact_amy)

    # PRINT OUT THE CONTACTS IN THE LIST
    print 'TEST ADDING CONTACTS'
    for contact in contacts_list:
        print contact.first_name, contact.last_name

    # PRINT OUT THE NAME OF THIS MODULE
    print "__name__ is " + __name__


    # TEST .sort() on a list of objects
    # print "SORT TEST 1"
    # contacts_list.sort()
    # for contact in contacts_list:
    #     print contact.first_name, contact.last_name

    print "SORT TEST 2"
    contacts_list.sort(key = attrgetter('last_name'))
    for contact in contacts_list:
        print contact.first_name, contact.last_name

    print "SORT TEST 3"
    contacts_list.sort(key = attrgetter('last_name', 'first_name'))
    for contact in contacts_list:
        print contact.first_name, contact.last_name


if __name__ == "__main__":
    main()
