import functools
from tkinter.constants import W
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    a_count, write_idx = 0, 0
    for i in range(size):
        if s[i] == 'a':
            a_count += 1
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1

    # backward iteration
    current_index = write_idx - 1
    write_idx = write_idx + a_count - 1
    final_size = write_idx +1
    while current_index >= 0:
        if s[current_index] == 'a':
            s[write_idx] = 'd'
            s[write_idx - 1] = 'd'
            write_idx -= 2
        else:
            s[write_idx] = s[current_index]
            write_idx-=1
        current_index-=1    
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
