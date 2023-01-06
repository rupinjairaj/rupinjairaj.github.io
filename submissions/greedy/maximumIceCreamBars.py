"""
Question: https://leetcode.com/problems/maximum-ice-cream-bars/
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        iceCreamBars = 0
        for cost in costs:
            if coins - cost >= 0:
                coins -= cost
                iceCreamBars += 1
            else:
                break
        return iceCreamBars


testCases = [
    {
        "costs":  [1, 3, 2, 4, 1],
        "coins": 7,
        "output": 4
    },
    {
        "costs":  [10, 6, 8, 7, 7, 8],
        "coins": 5,
        "output": 0
    },
    {
        "costs":  [1, 6, 3, 1, 2, 5],
        "coins": 20,
        "output": 6
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.maxIceCream(testCase["costs"], testCase["coins"])
    print(result)
