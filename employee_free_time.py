from typing import List
import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # sweep line + minheap
    # O(mlogn) time, where m is the number of schedules and n is the number of employees, bc the initial size of minheap is n, we need to heappush it m times in the while loop, and each heappush takes logn
    # O(n) space
    # similar to Meeting Rooms
    def employeeFreeTime(self, schedule: List[List[Interval]]):
        res = []
        minheap = [(emp[0].start, eid, 0) for eid, emp in enumerate(schedule)]
        heapq.heapify(minheap)
        last_end = -1
        while minheap:
            t, eid, i = heapq.heappop(minheap)
            if 0 <= last_end < t:
                res.append([last_end, t])
            last_end = max(last_end, schedule[eid][i].end)
            if i < len(schedule[eid]) - 1:
                heapq.heappush(minheap, (schedule[eid][i + 1].start, eid, i + 1))
        return res


    # sweep line + sorting, O(mlogm) time, O(m) space, not efficient compared to the minheap solution
    def employeeFreeTime1(self, schedule: List[List[Interval]]):
        res = []
        work = [(emp_i.start, eid, i) for eid, emp in enumerate(schedule) for i, emp_i in enumerate(emp)]
        work.sort()
        last_end = -1
        for t, eid, i in work:
            if 0 <= last_end < t:
                res.append([last_end, t])
            last_end = max(last_end, schedule[eid][i].end)
        return res
    
        

if __name__ == '__main__':
    schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    output = Solution().employeeFreeTime(schedule)
    print(output)
