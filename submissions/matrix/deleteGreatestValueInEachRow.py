"""
Question: https://leetcode.com/problems/delete-greatest-value-in-each-row/
"""
from typing import List
import sys


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for rowIdx in range(len(grid)):
            grid[rowIdx].sort()

        result = 0
        for colIdx in range(len(grid[0])):
            currMax = -sys.maxsize
            for rowIdx in range(len(grid)):
                currMax = max(currMax, grid[rowIdx][colIdx])
            result += currMax

        return result


testCases = [
    {
        "grid": [[1, 2, 4], [3, 3, 1]],
        "output": 8
    },
    {
        "grid": [[10]],
        "output": 10
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.deleteGreatestValue(testCase["grid"])
    print(result)
