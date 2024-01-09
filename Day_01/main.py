def read_data(filename) -> list:
    data = []
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            data.append(line)
            line = file.readline()

    return data


def get_calibration_value(string):
    value = 0
    first_digit = 0
    last_digit = 0
    digit_found = False

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for char in string:
        if char in digits:
            if digit_found:
                last_digit = int(char)
            else:
                first_digit = int(char)
                last_digit = int(char)
                digit_found = True

    if digit_found:
        value = 10 * first_digit + last_digit

    return value


def run_day_1_part_1(strings):
    sum_of_values = 0
    for line in strings:
        sum_of_values += get_calibration_value(line)
    return sum_of_values


def remove_digits(input_string):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for symbol in digits:
        input_string = input_string.replace(symbol, '')

    return input_string


def replace_words_with_digits(input_string):
    test_digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    for digit, word in test_digits.items():
        input_string = input_string.replace(word, str(digit))

    return input_string

def find_first_word_position(input_string):
    test_digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    position = -1
    found_digit = -1

    for digit, word in test_digits.items():
        

    return position, found_digit

def run_day_1_part_2(strings):
    sum_of_values = 0
    i = 0
    for line in strings:
        i = i + 1
        print(line)
        modified_line = replace_words_with_digits(line)
        print(modified_line)
        val = get_calibration_value(modified_line)
        print(val)
        sum_of_values += val
        if i > 15:
            break

    return sum_of_values


if __name__ == '__main__':
    list_of_strings = read_data("test.txt")

    """
    result1 = run_day_1_part_1(list_of_strings)
    print("Total:")
    print(result1)"""

    result2 = run_day_1_part_2(list_of_strings)
    print("Total (2):")
    print(result2)
