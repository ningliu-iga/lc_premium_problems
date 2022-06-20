from typing import List


class Solution:
    # brute force: O(n^3) time, bc two loops and one string slicing, O(n^2) space b/o the set
    def longestRepeatingSubstring1(self, s: str) -> int:

        seen = set()
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1):
                sub_str = s[j:i + 1]
                if sub_str not in seen:
                    seen.add(sub_str)
                else:
                    ans = max(ans, len(sub_str))
        return ans


    # binary search for the longest length where findRepeatingSubstr returns True
    # TEMPLATE for binary search: every time we have l=m, we do a +1 when calculating m
    # O(n^2*logn) time: binary search is logn, each findRepeatingSubstr takes n^2
    # O(n^2) space, b/o the set in which we have n-length+1 number of strings of len(length)
    def longestRepeatingSubstring(self, s: str) -> int:
        def findRepeatingSubstr1(length):
            seen = set()
            for i in range(n - length + 1):
                sub_str = s[i:i + length]
                if sub_str in seen:
                    return True
                seen.add(sub_str)
            return False

        # simple improvement of space complexity from O(n^2) to O(n): instead of storing the substrings, we can store
        # the hash value of the string.
        def findRepeatingSubstr(length):
            seen = set()
            for i in range(n - length + 1):
                h = hash(s[i:i + length])
                if h in seen:
                    return True
                seen.add(h)
            return False
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            # m = (l + r + 1) // 2 below is better implementation to avoid possible overflow
            # +1 is to avoid infinite loop where l=3 is True and r=4 is False (m will always be 3)
            m = l + (r - l + 1) // 2
            if findRepeatingSubstr(m):
                l = m
            else:
                r = m - 1
        return l # return r is good too, bc the while loop exits when l==r

if __name__ == '__main__':
    input = ["abcd", "abbaba", "aabcaabdaab", "aaaaa"]
    expect = [0, 2, 3, 4]
    output = list(map(Solution().longestRepeatingSubstring, input))
    if expect == output:
        print('Accepted')
    else:
        print('Wrong')
        print(output)
