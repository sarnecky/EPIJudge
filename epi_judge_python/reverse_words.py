import functools
from tracemalloc import start

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    reverse_range(s, 0, len(s) - 1) # first of all, reverse entire stirng

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish+=1
        
        if finish == len(s):
            break

        reverse_range(s, start, finish -1)

        start = finish+1
    reverse_range(s, start, len(s) - 1) # reverse laset word


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
