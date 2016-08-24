import contact
# Exercise Part 2 - Importing a class as a module


def main():
    # create a list to hold contacts
    contacts_list = []

    # prompt user to add a new contact.
    # prompt for each of the details and save the response.
    print "Add new contact"
    first = raw_input("What is the first name?")
    last = raw_input("What is the last name?")
    mobile = raw_input("What is your cell number?")
    email = raw_input("What is your email?")

    # create a new contact
    new_contact = contact.Contact(last_name=last, first_name=first, mobile_phone=mobile, email=email)

    # add contact to the list
    contacts_list.append(new_contact)

    # print out the contact info in the list.
    for info in contacts_list:
        print info.first_name
        print info.last_name
        print info.mobile_phone
        print info.email


if __name__ == "__main__":
    main()