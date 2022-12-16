"""
Question: https://leetcode.com/problems/find-pivot-index/description/
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        nums.append(0)
        prefixSum = {}

        currSum = 0
        for idx, num in enumerate(nums):
            currSum += num
            prefixSum[idx] = currSum

        leftSum = 0

        numsLength = len(nums) - 1
        for idx in range(numsLength):
            if leftSum == prefixSum[numsLength] - prefixSum[idx]:
                return idx
            leftSum += nums[idx]

        return -1


testCases = [
    {
        "nums": [1, 7, 3, 6, 5, 6],
        "output": 3,
    },
    {
        "nums": [1, 2, 3],
        "output": -1
    },
    {
        "nums": [2, 1, -1],
        "output": 0
    },
    {
        "nums": [-1, -1, 0, 1, 1, 0],
        "output": 5
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.pivotIndex(testCase["nums"])
    print(result)
