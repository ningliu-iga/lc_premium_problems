from typing import List


class Solution:
    # dp: O(n) time, O(1) space
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])


if __name__ == '__main__':
    input = [[17,2,17],[16,16,5],[14,3,19]]
    output = Solution().minCost(input)
    print(output)
