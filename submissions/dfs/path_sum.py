"""
Question: https://leetcode.com/problems/path-sum/description/
"""
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        def isLeaf(node: TreeNode):
            return node.left is None and node.right is None

        def dfs(node: TreeNode, currSum: int, target: int) -> bool:

            currSum += node.val

            if currSum == target and isLeaf(node):
                return True

            if node.left is not None and dfs(node.left, currSum, target):
                return True

            if node.right is not None and dfs(node.right, currSum, target):
                return True

            return False

        return True if dfs(root, 0, targetSum) else False


test_cases = [
    {
        "root": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1],
        "targetSum": 22,
        "output": True,
    },
    {
        "root": [1, 2, 3],
        "targetSum": 5,
        "output": False,
    },
    {
        "root": [],
        "targetSum": 0,
        "output": False,
    },
    {
        "root": [1, 2],
        "targetSum": 1,
        "output": False,
    },
]


def buildTree(idx: int, node: TreeNode, nums: List[int]):

    left_idx = (idx * 2) + 1
    if left_idx < len(nums) and nums[left_idx] is not None:
        node.left = TreeNode(nums[left_idx])
        buildTree(left_idx, node.left, nums)

    right_idx = (idx * 2) + 2
    if right_idx < len(nums) and nums[right_idx] is not None:
        node.right = TreeNode(nums[right_idx])
        buildTree(right_idx, node.right, nums)


for test_case in test_cases:
    runner = Solution()
    values = test_case["root"]
    root = None
    if len(values) != 0:
        root = TreeNode(values[0])
        buildTree(0, root, values)
    print(runner.hasPathSum(root, test_case['targetSum']))
