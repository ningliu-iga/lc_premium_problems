from typing import List
import heapq


class Solution:
    # save all meetings in events with [start, 1] and [end, -1], then sort events, then loop over events, and count the number of rooms needed each time and update the max room needed.
    # O(nlogn) time, O(n) space
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        events = []
        for s, e in intervals:
            events += [s, 1], [e, -1]
        events.sort()
        n_rooms = curr = 0
        for _, taken in events:
            curr += taken
            n_rooms = max(n_rooms, curr)
        return n_rooms

    # minheap: loop over intervals, if minheap is not empty and its first element is less than or equal to the start time of the current meeting, pop minheap[0] out. then heappush the current end time.
    # O(nlogn) time, O(n) space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minheap = []
        for interval in intervals:
            if minheap and interval[0] >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval[1])
        return len(minheap)


if __name__ == '__main__':
    schedule = [[0,30],[5,10],[15,20]]
    output = Solution().minMeetingRooms(schedule)
    print(output)
