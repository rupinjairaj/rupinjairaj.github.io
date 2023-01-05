"""
Question: https://leetcode.com/problems/find-k-closest-elements/
"""
from typing import List
import sys


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lowIndex = 0
        highIndex = len(arr) - 1

        while highIndex - lowIndex >= k:
            if abs(arr[lowIndex] - x) > abs(arr[highIndex] - x):
                lowIndex += 1
            else:
                highIndex -= 1

        return arr[lowIndex: highIndex+1]


testCases = [
    {
        "arr":  [1, 2, 3, 4, 5],
        "k":  4,
        "x":  3,
        "output": [1, 2, 3, 4]
    },
    {
        "arr":  [1, 2, 3, 4, 5],
        "k":  4,
        "x": -1,
        "output": [1, 2, 3, 4]
    },
    {
        "arr":  [1, 1, 1, 10, 10, 10],
        "k":  1,
        "x": 9,
        "output": [10]
    },
    {
        "arr":  [1],
        "k":  1,
        "x": 1,
        "output": [1]
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.findClosestElements(
        testCase["arr"], testCase["k"], testCase["x"])
    print(result)
