def read_data() -> list:
    data = []
    with open("data.txt", "r") as file:
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


if __name__ == '__main__':
    list_of_strings = read_data()

    result = run_day_1_part_1( list_of_strings )
    print("Total:")
    print(result)
