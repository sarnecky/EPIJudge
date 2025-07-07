from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        is_negative, x = True, -x
    result = []
    while True:
        character = x % 10
        result.append(chr(ord('0') +character))
        x //= 10
        if x  == 0:
            break
    response = ('-' if is_negative else '') + ''.join(reversed(result))
    return response


def string_to_int(input_string: str) -> int:
    sign =  -1 if input_string[0] == '-' else 1
    result = 0
    for i in input_string[1:] if input_string[0] in '-+' else input_string:
        result = result*10 + string.digits.index(i)
    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
