"""
Question: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
"""
from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskDifficulties = Counter(tasks)

        if 1 in taskDifficulties.values():
            return -1

        result = 0

        for val in taskDifficulties.values():
            result += val//3 + (1 if val%3 else 0)

        return result


testCases = [
    {
        "tasks": [2, 2, 3, 3, 2, 4, 4, 4, 4, 4],
        "output": 4
    },
    {
        "tasks": [2, 3, 3],
        "output": -1
    },
    {
        "tasks": [7, 7, 7, 7, 7, 7],
        "output": 2
    },
    {
        "tasks": [69, 65, 62, 64, 70, 68, 69, 67, 60, 65, 69, 62, 65, 65, 61, 66, 68, 61, 65, 63, 60, 66, 68, 66, 67, 65, 63, 65, 70, 69, 70, 62, 68, 70, 60, 68, 65, 61, 64, 65, 63, 62, 62, 62, 67, 62, 62, 61, 66, 69],
        "output": 21
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.minimumRounds(testCase["tasks"])
    print(result)
