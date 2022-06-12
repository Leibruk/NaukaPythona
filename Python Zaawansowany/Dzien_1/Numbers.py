values = range(int(input()), int(input()) + 1)
numbers = []
for i in values:
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(i)


def prettify_print(numbers):
    """Wypisywwanie 5 liczb w linii

    :param numbers: Lista liczb do wypisania
    :return:
    """

    max_numbers_in_one_line = 5
    current_numbers_in_line = 0

    for number in numbers:
        if current_numbers_in_line == max_numbers_in_one_line:
            print()
            current_numbers_in_line = 0
        print(number, end=' ')
        current_numbers_in_line += 1

prettify_print(values)