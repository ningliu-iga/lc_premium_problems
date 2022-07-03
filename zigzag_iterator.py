from typing import List
import itertools


class ZigzagIterator(object):
    # using generator, O(n) time and space
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)


    def next(self):
        """
        :rtype: int
        """
        self.n -= 1
        return next(self.vals)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0


if __name__ == '__main__':
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]

    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext(): v.append(i.next())

    expect = [1, 3, 2, 4, 5, 6]
    if expect == v:
        print('Accepted')
    else:
        print('Wrong')
        print(v)
