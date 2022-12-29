"""
Question: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        windowSize = 3
        charactersInCurrentWindow = set()
        result = 0
        for idx in range(len(s)):
            if len(charactersInCurrentWindow) == windowSize:
                result += 1
            currWindowEndPosition = idx+windowSize
            if currWindowEndPosition > len(s):
                break
            charactersInCurrentWindow = set(s[idx: currWindowEndPosition])

        return result


testCases = [
    {
        "s": "xyzzaz",
        "output": 1
    },
    {
        "s": "aababcabc",
        "output": 4
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.countGoodSubstrings(testCase["s"])
    print(result)
