from typing import List
import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.m = collections.deque()
        self.size = size
        self.total = 0

    # O(1) time, O(size) space
    def next(self, val: int) -> float:
        self.m.append(val)
        self.total += val
        if len(self.m) > self.size:
            self.total -= self.m.popleft()
        return self.total / len(self.m)


if __name__ == '__main__':
    m = MovingAverage(3)

    inp = [1, 10, 3, 5]
    expect = [1, 5.5, 14/3, 6]
    out = list(map(m.next, inp))
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
