"""
Question: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
from collections import Counter


# Divide and conquer approach
class Solution1:
    def longestSubstring(self, s: str, k: int) -> int:

        counter = Counter(s)
        sLength = len(s)
        for idx in range(sLength):
            if counter[s[idx]] >= k:
                continue
            return max(self.longestSubstring(s[:idx], k),
                       self.longestSubstring(s[idx+1:], k))
        return len(s)


testCases = [
    {
        "s": "aaabb",
        "k":  3,
        "output": 3
    },
    {
        "s": "ababbc",
        "k":  2,
        "output": 5
    }
]

for testCase in testCases:
    runner = Solution1()
    result = runner.longestSubstring(testCase["s"], testCase["k"])
    print(result)
