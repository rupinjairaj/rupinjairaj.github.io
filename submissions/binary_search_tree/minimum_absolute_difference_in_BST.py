"""
Question: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
from typing import Optional, List
import sys
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def preOrderTraversal(node: TreeNode, node_list: List[int]):
            if node is None:
                return

            preOrderTraversal(node.left, node_list)
            node_list.append(node.val)
            preOrderTraversal(node.right, node_list)

        sorted_node_list = []
        preOrderTraversal(root, sorted_node_list)

        result = sys.maxsize
        for idx in range(1, len(sorted_node_list)):
            result = min(result, abs(sorted_node_list[idx]) - abs(sorted_node_list[idx-1]))

        return result


test_cases = [
    {
        "root": [4, 2, 6, -1, 3],
        "output": 1
    },
    {
        "root": [1, 0, 48, None, None, 12, 49],
        "output": 1
    }
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
    print(runner.getMinimumDifference(root))
