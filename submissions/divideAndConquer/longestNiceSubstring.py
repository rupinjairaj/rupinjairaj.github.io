"""
Question: https://leetcode.com/problems/longest-nice-substring/
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        # if len(s) < 2:
        #     return ""

        charactersInS = set(s)

        for idx, c in enumerate(s):
            if not (c.lower() in charactersInS and c.upper() in charactersInS):
                s1 = self.longestNiceSubstring(s[:idx])
                s2 = self.longestNiceSubstring(s[idx+1:])
                return s2 if len(s2) > len(s1) else s1

        return s


testCases = [
    {
        "s":  "YazaAay",
        "output": "aAa"
    },
    {
        "s":  "Bb",
        "output": "Bb"
    },
    {
        "s":  "c",
        "output": ""
    },
    {
        "s":  "dDzeE",
        "output": "dD"
    },
    {
        "s":  "ijIJwuUnW",
        "output": "ijIJ"
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.longestNiceSubstring(testCase["s"])
    print(result)
