"""
Question: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSums = []
        for rowIdx in range(len(matrix)):
            currRow = matrix[rowIdx]
            tempPrefixSum = [0]
            currSum = 0
            for colIdx in range(len(currRow)):
                currSum += currRow[colIdx]
                tempPrefixSum.append(currSum)
            self.prefixSums.append(tempPrefixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for row in range(row1, row2+1):
            result += (self.prefixSums[row][col2+1] -
                       self.prefixSums[row][col1])
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
testCases = [
    {
        "numMatrix": [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ],
        "queries":[
            [2, 1, 4, 3],
            [1, 1, 2, 2],
            [1, 2, 2, 4]
        ],
        "output":[None, 8, 11, 12]
    }
]

for testCase in testCases:
    runner = NumMatrix(testCase["numMatrix"])
    # print(runner.prefixSums)
    for query in testCase["queries"]:
        row1, col1, row2, col2 = query
        result = runner.sumRegion(row1, col1, row2, col2)
        print(result)
