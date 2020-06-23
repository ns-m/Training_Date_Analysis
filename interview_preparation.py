"""
поиск дубликатов в списке
"""

def contain_duplicate(example_list):
    return len(set(example_list)) != len(example_list)

# print(contain_duplicate([1, 2, 3, 10]))

"""
Найти сумма цифр числа
"""

# def sum_of_numbers(some_number):
#     list = []
#     try:
#         for _ in str(some_number):
#             list.append(int(_))
#         print(sum(list))
#     except ValueError:
#         print('NaN!')

def sum_of_numbers(some_number):
    try:
        return sum([int(i) for i in str(some_number)])
    except ValueError:
        print('NaN!')

# sum_of_numbers('erte')

"""
Данно целое число. Максимальное число, от размера длинны числа.
4 - 9999, 2 - 99, 1 - 9 [int(i.replace(i,'9')) for i in str(some_digit)]
"""

def largest_number(some_digit):
    # dig = ""
    # for _ in range(some_digit):
    #     dig +=(str(_).replace(str(_), '9'))
    # return dig
    return 10 ** some_digit - 1

# print(largest_number(4))