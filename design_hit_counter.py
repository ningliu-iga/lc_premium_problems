from typing import List
import collections


# use a deque of list to store [timestamp, counts], where counts >=1, i.e., when the current timestamp equals dq[-1][0],
# we don't have to append new hits to the deque.
# amortized O(1) time, O(k) space
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq = collections.deque()
        self.count = 0
        self.k = 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.getHits(timestamp)
        if self.dq and self.dq[-1][0] == timestamp:
            self.dq[-1][1] += 1
        else:
            self.dq.append([timestamp, 1])
        self.count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.dq and self.dq[0][0] <= timestamp - self.k:
            self.count -= self.dq.popleft()[1]
        return self.count


if __name__ == '__main__':
    counter = HitCounter()
    out = []
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    out += counter.getHits(4),
    counter.hit(300)
    out += counter.getHits(300),
    out += counter.getHits(301),

    expect = [3,4,3]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
