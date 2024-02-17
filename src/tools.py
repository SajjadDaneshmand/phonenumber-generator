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
        csv_reader = list(csv.reader(csvfile))[1:]
        csv_values = []

        for i in csv_reader:
            if i:
                csv_values.append(i[0])

        csv_values.sort()
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


def to_csv(path, data):
    data = data.strip()
    with open(path, 'a') as file:
        file = csv.writer(file)
        return file.writerow([data])


def del_from_csv(path, data):
    rows = read_prefix_from_csv(path)

    try:
        rows.remove(data)
    except ValueError:
        return

    corrected_rows = [[row] for row in rows]
    corrected_rows.insert(0, ['code'])

    with open(path, 'w') as out:
        writer = csv.writer(out)
        return writer.writerows(corrected_rows)


def check_prefix(prefix: str):
    prefix = prefix.strip()
    chars = string.ascii_letters + string.punctuation
    if not prefix:
        return False

    for char in prefix:
        if char in chars:
            return False
    return True
