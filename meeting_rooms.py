from typing import List


class Solution:
    # sort the intervals by start time, then loop over the sorted intervals, if the current one starts before the
    # previous one ends, return False
    # O(nlogn) time, O(1) space
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]: return False
        return True


if __name__ == '__main__':
    schedule = [[0,30],[5,10],[15,20]]
    output = Solution().canAttendMeetings(schedule)
    print(output)
