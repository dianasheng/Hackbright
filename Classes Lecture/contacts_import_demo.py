import contact


def main():

    new_contact = contact.Contact(first_name="Diana", last_name="Smith", mobile_phone="555-555-5555")
    new_contact.last_name = "Banana"

    print new_contact.mobile_phone
    print new_contact.first_name


if __name__ == "__main__":
    main()