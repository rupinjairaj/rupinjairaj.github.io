"""
Question: https://leetcode.com/problems/subarray-sums-divisible-by-k/
"""
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remaindersSeen = {0: 1}

        currSum = 0
        result = 0
        for num in nums:
            currSum += num
            currRemainder = currSum % k
            if currRemainder in remaindersSeen:
                result += remaindersSeen[currRemainder]
                remaindersSeen[currRemainder] += 1
            else:
                remaindersSeen[currRemainder] = 1

        return result


testCases = [
    {
        "nums": [4, 5, 0, -2, -3, 1],
        "k": 5,
        "output": 7
    },
    {
        "nums": [5],
        "k": 9,
        "output": 0
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.subarraysDivByK(testCase["nums"], testCase["k"])
    print(result)
