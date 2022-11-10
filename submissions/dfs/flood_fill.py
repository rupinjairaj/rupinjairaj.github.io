"""
Question: https://leetcode.com/problems/flood-fill/
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        row = len(image)
        col = len(image[0])

        visited = []
        for i in range(row):
            row_elements = []
            for j in range(col):
                row_elements.append(False)
            visited.append(row_elements)

        def dfs(r, c, target, visited):

            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or visited[r][c] or image[r][c] != target:
                return

            if image[r][c] == target:
                # print(visited[r][c])
                visited[r][c] = True
                image[r][c] = color

                for direction in directions:
                    dfs(r + direction[0], c + direction[1], target, visited)

        dfs(sr, sc, image[sr][sc], visited)
        return image


test_cases = [
    {
        'image': [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 'sr': 1, 'sc': 1, 'color': 2,
        'output': [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    },
    {
        'image': [[0, 0, 0], [0, 0, 0]], 'sr': 0, 'sc': 0, 'color': 0,
        'output': [[0, 0, 0], [0, 0, 0]]
    }
]


for test_case in test_cases:
    runner = Solution()
    print(runner.floodFill(
        test_case['image'], test_case['sr'], test_case['sc'], test_case['color']))
