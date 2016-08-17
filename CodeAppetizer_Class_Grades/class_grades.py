'''
Converts a numerical score to a letter.
Scores are in a text file.
'''


def convert_score_to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def process_file_to_list():
    with open("class_grades.txt") as class_file:
        file_list = class_file.readlines()

    return file_list


def main():
    grade_list = process_file_to_list()

    for score in grade_list:
        letter = convert_score_to_letter(int(score.strip()))
        print score.strip() + " is a " + letter


if __name__ == '__main__':
    main()


