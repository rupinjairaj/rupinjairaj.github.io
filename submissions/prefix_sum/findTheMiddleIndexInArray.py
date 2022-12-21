"""
Question: https://leetcode.com/problems/find-the-middle-index-in-array/
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        prefixSums = []
        currSum = 0
        for num in nums:
            currSum += num
            prefixSums.append(currSum)

        for idx in range(0, len(nums) - 1):
            leftSum = prefixSums[idx]
            rightSum = prefixSums[-1] - prefixSums[idx+1]
            if idx == 0 and prefixSums[-1] - prefixSums[0] == 0:
                return 0
            if idx == len(nums) - 1 and prefixSums[-2] == 0:
                return len(nums) - 1
            leftSum = prefixSums[idx]
            rightSum = prefixSums[-1] - prefixSums[idx+1]
            if leftSum == rightSum:
                return idx+1

        return -1


class Solution2:
    def findMiddleIndex(self, nums: List[int]) -> int:

        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            if left == right - nums[idx]:
                return idx
            left += num
            right -= num
        return -1


testCases = [
    {
        "nums": [2, 3, -1, 8, 4],
        "output": 3
    },
    {
        "nums": [1, -1, 4],
        "output": 2
    },
    {
        "nums": [2, 5],
        "output": -1
    },
    {
        "nums": [1, 1, 1, 1],
        "output": -1
    },
    {
        "nums": [1],
        "output": 0
    },
    {
        "nums": [4, 0],
        "output": 0
    },
    {
        "nums": [3, 2, -1, -4, 8],
        "output": 1
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.findMiddleIndex(testCase["nums"])
    print(result)
