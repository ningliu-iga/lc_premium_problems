from typing import List
import heapq
import collections


class Solution:
    # maxheap, O(nlogn) time (push and pop in maxheap both take logn), O(n) space
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for id, score in items:
            heapq.heappush(dic[id], -score)
        res = []
        for id, scores in dic.items():
            high_five = 0
            for _ in range(5):
                high_five -= heapq.heappop(scores)
            res.append([id, high_five // 5])
        return res


if __name__ == '__main__':
    inp = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    out = Solution().highFive(inp)

    expect = [[1,87],[2,88]]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
