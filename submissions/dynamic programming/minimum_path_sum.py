"""
Question: https://leetcode.com/problems/minimum-path-sum/
"""
from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        prev = 0
        for c in range(len(grid[0])):
            grid[0][c] = prev + grid[0][c]
            prev = grid[0][c]

        prev = 0
        for r in range(len(grid)):
            grid[r][0] = prev + grid[r][0]
            prev = grid[r][0]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = min(grid[r - 1][c], grid[r][c - 1]) + grid[r][c]

        return grid[-1][-1]


test_cases = [{
    "grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
    "output": 7
}, {
    "grid": [[1, 2, 3], [4, 5, 6]],
    "output": 12
}]

for test_case in test_cases:
    runner = Solution()
    print(runner.minPathSum(test_case["grid"]))
