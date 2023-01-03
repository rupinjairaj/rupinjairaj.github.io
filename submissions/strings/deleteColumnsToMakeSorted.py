"""
Question: https://leetcode.com/problems/delete-columns-to-make-sorted/
"""
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columnCount = len(strs[0])
        result = 0
        for columnIndex in range(columnCount):
            charactersInCurrentColumn = [
                strs[index][columnIndex] for index in range(len(strs))]
            sortedCharacters = sorted(charactersInCurrentColumn)
            for i in range(len(charactersInCurrentColumn)):
                if charactersInCurrentColumn[i] != sortedCharacters[i]:
                    result += 1
                    break
        return result


class Solution2:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                c += 1
        return c


testCases = [
    {
        "strs": ["cba", "daf", "ghi"],
        "output": 1
    },
    {
        "strs": ["a", "b"],
        "output": 0
    }, {
        "strs": ["zyx", "wvu", "tsr"],
        "output": 3
    }
]

for testCase in testCases:
    runner = Solution2()
    result = runner.minDeletionSize(testCase["strs"])
    print(result)
