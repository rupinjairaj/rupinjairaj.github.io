"""
Question: https://leetcode.com/problems/continuous-subarray-sum/
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderToPrefixSumIndex = {0: [0]}

        currSum = 0
        for idx, num in enumerate(nums):
            currSum += num
            currRemainder = currSum % k
            if currRemainder in remainderToPrefixSumIndex:
                remainderToPrefixSumIndex[currRemainder].append(idx+1)
                indicies = remainderToPrefixSumIndex[currRemainder]
                if indicies[-1] - indicies[0] >= 2:
                    return True
            else:
                remainderToPrefixSumIndex[currRemainder] = [idx+1]

        return False


testCases = [
    {
        "nums": [23, 2, 4, 6, 7],
        "k": 6,
        "output": True
    },
    {
        "nums": [23, 2, 6, 4, 7],
        "k": 6,
        "output": True
    },
    {
        "nums": [23, 2, 6, 4, 7],
        "k": 13,
        "output": False
    },
    {
        "nums": [23, 2, 4, 6, 6],
        "k": 7,
        "output": True
    },
    {
        "nums": [1],
        "k": 1,
        "output": False
    },
    {
        "nums": [1, 0],
        "k": 2,
        "output": False
    },
    {
        "nums": [5, 0, 0, 0],
        "k": 3,
        "output": True
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.checkSubarraySum(testCase["nums"], testCase["k"])
    print(result)
