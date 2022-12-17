"""
Question: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSums = []
        currSum = 0

        for idx, num in enumerate(nums):
            currSum += num
            prefixSums.append(currSum)

        minValue = min(min(prefixSums), 1)
        return minValue if minValue > 0 else (-1*minValue)+1


testCases = [
    {
        "nums": [-3, 2, -3, 4, 2],
        "output": 5
    },
    {
        "nums": [1, 2],
        "output": 1
    },
    {
        "nums": [1, -2, -3],
        "output": 5
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.minStartValue(testCase["nums"])
    print(result)
