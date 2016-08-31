# import contact
import contact

def main():
    # create an instance of Contact
    new_contact = contact.Contact(first_name = "Diana", last_name = "Banana",mobile_phone = "555-555-5000")
    # change an attribute
    new_contact.last_name = "Smith"
    # call a method
    new_contact.send_text("Hello! How are you?")

    # print the attributes
    # print new_contact
    print new_contact.first_name
    print new_contact.last_name
    print new_contact.mobile_phone

if __name__ == '__main__':
    main()