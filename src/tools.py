import datetime
import string
import time
import csv
import gc


def check_format(phonenumber: str):
    # check point 1
    if len(phonenumber) != 11:
        return False

    # check point 2
    if not phonenumber.startswith('09'):
        return False

    # check point 3
    if '*' not in phonenumber:
        return False

    # check point 4
    for digit in phonenumber:
        if digit not in string.digits + '*':
            return False

    return True


def read_prefix_from_csv(path: str):
    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_values = [i[0] for i in list(csv_reader)][1:]
        return csv_values


def general_generator(raw_phonenumber: str):
    return str(int(raw_phonenumber) + 1)


def under_one_generator(raw_phonenumber: str):
    return str(int('1' + raw_phonenumber) + 1)[1:]


def replace_nums(main_phonenumber: str, replacement: str, indexes: list):
    main_phonenumber = list(main_phonenumber)
    for index, i in enumerate(replacement):
        main_phonenumber[indexes[index]] = i
    return ''.join(main_phonenumber)


def divide_number(number, range_num):
    divider = number // range_num
    remainder = number % range_num
    return divider, remainder


def clear_ram(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        gc.collect()
    return wrapper


def func_runtime(func):
    def wrapper(*args, **kwargs):
        first_time = time.time()
        func(*args, **kwargs)
        last_time = time.time()
        return datetime.timedelta(seconds=last_time - first_time)

    return wrapper


@func_runtime
def do():
    for i in range(100000000):
         continue

s = do()
print(s)