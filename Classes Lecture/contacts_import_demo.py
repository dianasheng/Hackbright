import contact


def main():
    # create an instance of Contact
    new_contact = contact.Contact(first_name="Diana", last_name="Smith", 
        mobile_phone="555-555-5555")

    # change an attribute
    new_contact.last_name = "Banana"

    #call a method
    new_contact.send_text("Hello, everyone!")
    new_contact.send_email("Hey what's up?")
    # print the attributes
    print new_contact.mobile_phone
    print new_contact.last_name


if __name__ == "__main__":
    main()
