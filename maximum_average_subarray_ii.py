from typing import List


class Solution:
    # binary search for the max average. the left and right bounds of the binary search are the min(nums) and max(nums),
    # respectively, since no average can be smaller than min(nums) and no average can be larger than max(nums). For each
    # middle value, we check if there is a contiguous subarray of length at least k whose average is greater than or
    # equal to the middle value.
    # in the helper function, we loop over nums, to compute the current sum, we add num - m so that we can directly
    # check if the sum>=0. when the subarray length is greater than k, we consider subtracting the left smaller subarrays.
    # O(nlog((max-min)/1e-5)), bc binary search is logN=log((max-min)/1e-5), within each helper function, there is a
    # for loop that takes n. O(1) space
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def found(m):
            curr = pre_sum = min_pre_sum = 0
            for i, v in enumerate(nums):
                curr += v - m
                if i >= k:
                    pre_sum += nums[i - k] - m
                    min_pre_sum = min(min_pre_sum, pre_sum)
                if i >= k - 1 and curr - min_pre_sum >= 0:
                    return True
            return False

        l, r = min(nums), max(nums)
        while r - l > 1e-5:
            m = l + (r - l) / 2
            if found(m):
                l = m
            else:
                r = m
        return l


if __name__ == '__main__':
    inp = [1, 12, -5, -6, 50, 3]
    out = Solution().findMaxAverage(inp, 4)

    expect = 12.75
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
