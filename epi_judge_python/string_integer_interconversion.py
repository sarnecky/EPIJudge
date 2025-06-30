from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        character = chr(ord('0') + x % 10)
        s.append(character)
        x //= 10
        if x == 0:
            break
    
    return ('-' if is_negative else '') + ''.join(reversed(s));


def string_to_int(input_string: str) -> int:
    sign = -1 if input_string[0] == '-' else 1
    
    if input_string[0] in ('+', '-'):
        input_string = input_string[1:]

    return sign * functools.reduce(
        lambda running_sum, character: running_sum * 10 + string.digits.index(character), input_string, 0)


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
