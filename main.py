# MarkS - Python Challenge Day 07 -  SlackAdder

def integer_list(number_string):
    integer_stripped = [int(x) for x in number_string.split(',')]
    return integer_stripped


def slack_adder(integer_numbers, target_integer):
    list_length = len(integer_numbers)
    for i in range(list_length):
        for j in range(i+1, list_length):
            if integer_numbers[i] + integer_numbers[j] == target_integer:
                return i, j


input_numbers = input("Please input a list of numbers: ")
input_target = input("Please input a target sum: ")

print(slack_adder(integer_list(input_numbers), int(input_target)))
