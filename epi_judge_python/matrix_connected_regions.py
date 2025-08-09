import collections
from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    queue = collections.deque([(x, y)])
    current_color = image[x][y]
    while queue:
        x, y = queue.popleft()
        image[x][y] = not current_color

        for next_x, next_y in ((x, y +1), (x, y - 1), (x +1, y), (x - 1, y)):
            if (0 <= next_x < len(image) and
                0 <= next_y < len(image[next_x]) and
                image[next_x][next_y] == current_color):
                    queue.append((next_x, next_y))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
