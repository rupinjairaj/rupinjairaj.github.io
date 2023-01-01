"""
Question: https://leetcode.com/problems/range-sum-of-bst/
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        pass


testCases = [
    {
        "root": [10, 5, 15, 3, 7, None, 18],
        "low": 7,
        "high": 15,
        "output": 32
    },
    {
        "root": [10, 5, 15, 3, 7, 13, 18, 1, None, 6],
        "low": 6,
        "high": 10,
        "output": 23
    }
]


def buildTree(root: List):
    return None


for testCase in testCases:
    runner = Solution()
    root = buildTree(testCase["root"])
    result = runner.rangeSumBST(root, testCase["left"], testCase["right"])
    print(result)
