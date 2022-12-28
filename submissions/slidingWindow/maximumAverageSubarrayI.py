"""
Question: https://leetcode.com/problems/maximum-average-subarray-i/
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[0:k])
        result = currSum

        for i in range(len(nums)):
            if i+k < len(nums):
                currSum = currSum - nums[i] + nums[i+k]
                result = max(result, currSum)

        return result/k


testCases = [
    {
        "nums":  [1, 12, -5, -6, 50, 3], "k": 4,
        "output": 12.75000
    },
    {
        "nums": [5], "k": 1,
        "output": 5.00000
    },
    {
        "nums": [-1], "k": 1,
        "output": -1.0
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.findMaxAverage(testCase["nums"], testCase["k"])
    print(result)
