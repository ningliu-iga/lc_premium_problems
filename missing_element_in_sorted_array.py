from typing import List


class Solution:
    # since brute force takes O(n), we need to find a solution better than brute force, so naturally we think about
    # binary search. we do binary search based on the number of missing numbers 'missing'. if 'missing' is greater than
    # k, then what we are looking for is to the left of the current index. if 'missing' is less than k, then it is to
    # the right of the current index. since we need to find the interval [nums[l], nums[r]] where 'missing' at l is
    # less than k and 'missing' at r is greater than or equal to k, the while condition is r-l>1 (when r-l==1, we find
    # this interval).
    # O(logn) time, O(1) space
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if (missing := nums[-1] - (nums[0] + n - 1)) < k: return nums[-1] + k - missing
        l, r = 0, n - 1
        while r - l > 1:
            m = (l + r) // 2
            missing = nums[m] - (nums[l] + m - l)
            if missing < k:
                l = m
                k -= missing
            else:
                r = m
        return nums[l] + k


if __name__ == '__main__':
    inp1 = [4, 7, 9, 10];
    k1 = 1
    inp2 = [4, 7, 9, 10];
    k2 = 3
    inp3 = [1, 2, 4];
    k3 = 3
    out = list(map(Solution().missingElement, (inp1, inp2, inp3), (k1, k2, k3)))

    expect = [5, 8, 6]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
