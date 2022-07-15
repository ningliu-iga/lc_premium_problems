from typing import List


class Solution:
    # binary search, O(nlogn) time, O(1) space
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def isCutPossible(m, k):
            for r in ribbons:
                k -= r // m
                if k <= 0: return True
            return False
        l, r = 0, max(ribbons)
        while l < r:
            m = l + (r - l + 1) // 2
            if isCutPossible(m, k):
                l = m
            else:
                r = m - 1
        return l


if __name__ == '__main__':
    inp1 = [[9,7,5], [7,5,9], [5,7,9]]
    inp2 = [3, 4, 22]
    out = list(map(Solution().maxLength, inp1, inp2))

    expect = [5, 4, 0]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
