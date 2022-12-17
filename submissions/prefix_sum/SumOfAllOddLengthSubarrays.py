"""
Question: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        prefixSum = [0]
        currSum = 0
        for num in arr:
            currSum += num
            prefixSum.append(currSum)

        idx = 3
        # return prefixSum
        result = 0
        while idx <= len(prefixSum):
            for j in range(idx, len(prefixSum)):
                result += (prefixSum[j] - prefixSum[j-idx])
            idx += 2

        return result + sum(arr)


testCases = [
    {
        "arr": [1, 4, 2, 5, 3],
        "output": 58
    },
    {
        "arr": [1, 2],
        "output": 3
    },
    {
        "arr": [10, 11, 12],
        "output": 66
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.sumOddLengthSubarrays(testCase["arr"])
    print(result)
