"""
Question: https://leetcode.com/problems/sum-of-left-leaves/
"""
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def bfs(node: TreeNode):

            queue = [(False, node)]  # (isLeftChild, node)

            result = 0
            while len(queue) != 0:
                queue_len = len(queue)
                for idx in range(queue_len):
                    isLeftChild, node = queue.pop(0)
                    if isLeftChild and node.left is None and node.right is None:
                        result += node.val
                        continue
                    if node.left is not None:
                        queue.append((True, node.left))
                    if node.right is not None:
                        queue.append((False, node.right))
            return result

        return bfs(root)


test_cases = [
    {
        "root": [3, 9, 20, None, None, 15, 7],
        "output": 24
    },
    {
        "root": [1],
        "output": 0
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
    print(runner.sumOfLeftLeaves(root))
