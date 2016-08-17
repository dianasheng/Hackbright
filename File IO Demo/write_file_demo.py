"""
Objective: Write a program that takes input and writes it to a file.
1) Write to file - choose overwrite file or append to file
2) Get user input in main()
"""
def write_to_file(file_name, text_string):
    # mode = w overwrites the file
    # mode = a appends to the end of the file
    with open(file_name, mode="a") as my_file:
        my_file.write(text_string)
        my_file.write('\n')


def main():
    file_name = "Expenses.txt"
    expense = raw_input("Enter the date, name of expense, and the cost")
    write_to_file(file_name, expense)


if __name__ == "__main__":
    main()
