from typing import List, Dict

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    nearest_distance = float('inf')
    word_to_last_occurrence: Dict[str, int] = {}
    for i, word in enumerate(paragraph):
        if word in word_to_last_occurrence:
            last_word_index = word_to_last_occurrence[word]
            nearest_distance = min(nearest_distance, i - last_word_index)
        word_to_last_occurrence[word] = i
    return - 1 if nearest_distance == float('inf') else int(nearest_distance)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
