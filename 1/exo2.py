import re


def get_first_digit(string, reverse=False):
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if reverse:
        digits = {k[::-1]: v for k, v in digits.items()}

    x = re.search("|".join(digits.keys()), string)
    if x:
        number = x.group()
        string = string.replace(number, digits[number])

    for c in string:
        try:
            first = int(c)
            return first
        except ValueError:
            pass


with open("1/input.txt", "r") as file:
    result = 0
    for line in file.readlines():
        first = get_first_digit(line)
        last = get_first_digit(line[::-1], True)
        result += int(f"{first}{last}")

print(result)
