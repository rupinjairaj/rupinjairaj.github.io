"""
Question: https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]

        return nums


testCases = [
    {
        "nums": [1, 2, 3, 4],
        "output": [1, 3, 6, 10]
    },
    {
        "nums": [1, 1, 1, 1, 1],
        "output": [1, 2, 3, 4, 5]
    },
    {
        "nums": [3, 1, 2, 10, 1],
        "output": [3, 4, 6, 16, 17]
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.runningSum(testCase["nums"])
    print(result)
