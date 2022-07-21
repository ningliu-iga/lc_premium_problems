from typing import List
import collections


class Solution:
    # two pointers, curr tracks the number of distinct characters in the current window
    # O(n) time and space
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        ans = 0
        i = curr = 0
        for j, c in enumerate(s):
            count[c] += 1
            if count[c] == 1:
                curr += 1
                while curr > k:
                    count[s[i]] -= 1
                    if count[s[i]] == 0: curr -= 1
                    i += 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    inp1 = ["eceba", "aa"]
    inp2 = [2, 1]
    out = list(map(Solution().lengthOfLongestSubstringKDistinct, inp1, inp2))

    expect = [3, 2]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
