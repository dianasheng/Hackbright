"""
Demo different ways to read a file.
- readline()
- readlines()
- read()
- iterate over a file object
- test all the function in main()
"""


# readline() - reads first line of file, returns a string
def read_file_first_line(file_name):
    with open(file_name) as my_file:
        line = my_file.readline()
        print type(line)
    return line


# readlines() - reads all the lines in the text and returns a list
def read_file_to_list(file_name):
    with open(file_name) as my_file:
        output_list = my_file.readlines()
        print type(output_list)
    return output_list


# read() - reads the entire file and returns a string
def read_file(file_name):
    with open(file_name) as my_file:
        read_output = my_file.read()
        print type(read_output)
        return read_output


# For line - iterate file object line by line
# strip whitespaces if necessary
# store and return to list
def read_file_by_iteration(file_name):
    output_list = []
    with open(file_name) as my_file:
        for line in my_file:
            clean_line = line.strip()  # remove the newline character
            output_list.append(clean_line)
    return output_list


def main():
    # test all the functions
    file_name = "Budget.txt"
    print read_file_first_line(file_name)
    print read_file_to_list(file_name)
    print read_file(file_name)
    print read_file_by_iteration(file_name)


if __name__ == "__main__":
    main()
