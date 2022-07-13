from typing import List


class Solution:
    # binary search the longest length of the repeating substring.
    # O(n^2*logn) time, bc binary search takes O(logn), within found, there is a for loop which takes n and the string
    # slicing takes O(n), so total is O(n^2*logn) time.
    # O(n) space
    def longestRepeatingSubstring1(self, S: str) -> int:
        n = len(S)
        def found(m):
            seen = set()
            for i in range(n - m + 1):
                tmp = S[i:i+m]
                if tmp in seen:
                    return True
                else:
                    seen.add(tmp)
            return False
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if found(m):
                l = m
            else:
                r = m - 1
        return l

    # use polynomial rolling hash to reduce time complexity to O(nlogn) time
    def longestRepeatingSubstring1(self, S: str) -> int:
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        def found(m):
            seen = set()
            h = 0
            for i in range(m):
                h += h * 26 + nums[i]
            seen.add(h)
            for i in range(1, n - m + 1):
                h = h * 26 - nums[i - 1] * 26**m + nums[i + m - 1]
                if h in seen:
                    return True
                else:
                    seen.add(h)
            return False
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if found(m):
                l = m
            else:
                r = m - 1
        return l

    # dp: dp[i][j] represents the longest common substring length between S[:i] and S[:j] with constraint j<i, since we
    # always want to use a larger index i to compare with a smaller index j (they cannot be equal)
    # O(n^2) time and space
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i):
                if S[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    inp = ["abcd", "abbaba", "aabcaabdaab", "aaaaa"]
    out = list(map(Solution().longestRepeatingSubstring, inp))

    expect = [0, 2, 3, 4]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
