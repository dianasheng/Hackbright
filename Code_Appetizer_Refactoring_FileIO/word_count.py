import string
import collections

INPUT_FILE_NAME = "TestFile.txt"
OUTPUT_FILE_NAME = "wordcount.txt"


def process_file_to_list(file_name):
    with open(file_name) as file_to_process:
        file_string = file_to_process.read().decode("utf-8-sig").encode("utf-8")

    return file_string


def count_words(file_string):
    word_count = {}
    new_string = file_string.translate(None, string.punctuation).lower()
    words_list = new_string.split()

    for word in words_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count


def write_to_file(word_count_dict, file_name):
    with open(file_name, mode="w+") as file1:
        for word in word_count_dict:
            file1.write(word + " - " + str(word_count_dict[word]) + "\r")


def sort_dict_by_key(original_dict):
    return collections.OrderedDict(sorted(original_dict.items(), key=lambda t: t[0]))


def sort_dict_by_item(original_dict):
    return collections.OrderedDict(sorted(original_dict.items(), key=lambda t: t[1]))


def main():
    file_list = process_file_to_list(INPUT_FILE_NAME)

    file_word_count_dict = count_words(file_list)
    dict_by_key = sort_dict_by_key(file_word_count_dict)
    dict_by_item = sort_dict_by_item(file_word_count_dict)

    write_to_file(dict_by_key, OUTPUT_FILE_NAME)
    #write_to_file(dict_by_item, OUTPUT_FILE_NAME)


if __name__ == "__main__":
    main()
