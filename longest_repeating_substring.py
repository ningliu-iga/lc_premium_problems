from typing import List


class Solution:
    # brute force: check if every substring involving the rightmost letter has been seen before, if not, add it to the seen set.
	# O(n^3) time, bc two loops and one string slicing, O(n^2) space b/o the set
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
        def findRepeatingSubstr1(length):
            seen = set()
            for i in range(n - length + 1):
                h = hash(s[i:i + length])
                if h in seen:
                    return True
                seen.add(h)
            return False
		
		# further improvement to remove string slicing using polynomial rolling hashing, so time complexity becomes
        # O(nlogn)
		# for rolling hash, we first need to convert characters to digits and store them in nums using ord() to find
		# the unicode of the character, then the hashing of the current window [d1, d2, d3] is: 
		# h=d1*26**(length-1)+d2*26**(length-2)+d3*26**(length-3), to update h, we need to remove the first item and add the new item.
		# we then check if this hashing is in seen.
        def findRepeatingSubstr(length):
            seen = set()
            h = 0
            for i in range(length):
                h = h * 26 + nums[i]
            seen.add(h)
            for i in range(1, n - length + 1):
                h = h * 26 - nums[i - 1] * 26 ** length + nums[i - 1 + length]
                if h in seen:
                    return True
                seen.add(h)
            return False

        nums = [ord(c) - ord('a') for c in s]
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
