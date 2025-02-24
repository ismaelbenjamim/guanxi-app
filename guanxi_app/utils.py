import random
import string


def generate_security_code():
    length = 6
    characters = string.digits
    code = ''.join(random.choices(characters, k=length))
    return code


def generate_temp_password():
    length = 8
    characters = string.digits + string.ascii_letters
    password = ''.join(random.choices(characters, k=length))
    return password
