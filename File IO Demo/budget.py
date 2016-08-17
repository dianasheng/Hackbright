
"""
Write a program that reads a file and stores the output into a dictionary
Objectives:
    1) Read a file
    2) Store the contents into a dictionary

1) Read the file
    - Examine the file
    - Read the file and return output
2) Store the contents into a data structure
    - Iterate over the list and parse out components
    - Store components into dictionary

* Use print statements to help with debugging

"""


def read_file(file_name):
    with open(file_name) as my_file:
        output_list = my_file.readlines()
        # print output_list
    return output_list


def process_file_to_dictionary(file_list):
    budget = {}
    for item in file_list:
        split_items = item.split(" - ")
        # print split_items
        budget_item = split_items[0]
        cost = float(split_items[1])
        # print budget_item, cost
        budget[budget_item] = cost
    return budget


def main():
    file_name = "Budget.txt"
    file_list = read_file(file_name)
    # print file_list
    budget = process_file_to_dictionary(file_list)
    print budget


if __name__ == "__main__":
    main()

