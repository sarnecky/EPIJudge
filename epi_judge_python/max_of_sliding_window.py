import functools
from typing import List

from queue_with_max import QueueWithMax
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class TrafficElement:
    def __init__(self, time: int, volume: float) -> None:
        self.time = time
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __eq__(self, value: object) -> bool:
        return self.volume == value.volume and self.time == value.time


def calculate_traffic_volumes(A: List[TrafficElement],
                              w: int) -> List[TrafficElement]:
    maximum_volumes = []
    sliding_window = QueueWithMax()
    for traffic_element in A:
        sliding_window.enqueue(traffic_element)
        while traffic_element.time - sliding_window.head().time > w:
            sliding_window.dequeue()
        maximum_volumes.append(TrafficElement(traffic_element.time, sliding_window.max().volume))
    return maximum_volumes


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_of_sliding_window.py',
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
