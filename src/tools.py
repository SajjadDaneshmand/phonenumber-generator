def check_format(phonenumber: str):
    if len(phonenumber) != 11:
        return False
    if not phonenumber.startswith('09'):
        return False
    return True

