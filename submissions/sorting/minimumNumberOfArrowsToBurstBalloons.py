"""
Question: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        result = 1
        currEnd = points[0][1]

        for start, end in points:
            if start > currEnd:
                currEnd = end
                result += 1

        return result


testCases = [
    {
        "points": [[10, 16], [2, 8], [1, 6], [7, 12]],
        "output": 2
    },
    {
        "points": [[1, 2], [3, 4], [5, 6], [7, 8]],
        "output": 4
    },
    {
        "points": [[1, 2], [2, 3], [3, 4], [4, 5]],
        "output": 2
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.findMinArrowShots(testCase["points"])
    print(result)
