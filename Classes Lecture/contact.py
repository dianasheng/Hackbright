# EXERCISE PART 1
# class definition for a Contact
class Contact(object):
    # initialize an instance of the object Contact
    # we can use optional parameters for certain attributes
    def __init__(self, first_name, last_name,
                 mobile_phone = "", work_phone = "", email = "", twitter_handle = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.twitter_handle = twitter_handle

    def send_tweet(self, message_string):
        if self.twitter_handle != "":
            print "To: %s - %s" % (self.twitter_handle, message_string)
        else:
            print "No twitter handle set."

    def send_text(self, message_string):
        if self.mobile_phone != "":
            print "To: %s - %s" % (self.mobile_phone, message_string)
        else:
            print "No mobile phone number."

    def send_email(self, message_string):
        if self.email != "":
            print "Sending message: %s to %s." % (message_string, self.email)
        else:
            print "No email address."


# EXERCISE PART 2: TESTING THE CONTACT CLASS
# Create two contacts and add them to a list.
# Print out the contacts to see that it worked.

def main():
    contacts_list = []

    print 'TEST ADDING CONTACTS to List'
    contact_diana = Contact("Diana", "Banana", mobile_phone="415-555-5000")
    contacts_list.append(contact_diana)

    contact_james = Contact("James", "Frank", email="james@frank.com")
    contacts_list.append(contact_james)

    contact_amy = Contact("Amy", "Banana", mobile_phone="415-555-5555")
    contacts_list.append(contact_amy)

    # PRINT OUT THE CONTACTS IN THE LIST
    # You must specify the attribute of contact that you want to print. ex: contact.first_name
    for info in contacts_list:
        print info.first_name, info.last_name, info.email, info.mobile_phone

    # SEND TEXT TO EACH CONTACT
    for info in contacts_list:
        info.send_text("Hello! How are you?")

if __name__ == "__main__":
    main()
