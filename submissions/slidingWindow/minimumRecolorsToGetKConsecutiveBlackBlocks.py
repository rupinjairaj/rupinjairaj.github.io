"""
Question: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""
from collections import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = 0
        for i in range(k):
            result += 1 if blocks[i] == "W" else 0

        currCount = result
        for idx in range(1, len(blocks)-k+1):
            # print("curr substring: ", blocks[idx: idx+k])

            currCount -= 1 if blocks[idx-1] == "W" else 0
            currCount += 1 if blocks[idx+k-1] == "W" else 0
            result = min(result, currCount)

        return result if result >= 0 else 0


testCases = [
    {
        "blocks": "WBBWWBBWBW",
        "k": 7,
        "output": 3
    },
    {
        "blocks": "WBWBBBW",
        "k": 2,
        "output": 0
    },
    {
        "blocks": "WWBBBWBBBBBWWBWWWB",
        "k": 16,
        "output": 6
    },
    {
        "blocks": "WBB",
        "k": 1,
        "output": 0
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.minimumRecolors(testCase["blocks"], testCase["k"])
    print(result)
