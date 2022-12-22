"""
Question: https://leetcode.com/problems/linked-list-random-node/
"""

# Definition for singly-linked list.

from typing import Optional, List
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        selectedValue = 0
        curr = self.head
        while curr:
            if random.random() < 1/scope:
                selectedValue = curr.val
            curr = curr.next
            scope += 1

        return selectedValue

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


testCases = [
    {
        "input": [1, 2, 3],
        "output": [None, 1, 3, 2, 2, 3]
    }
]


def buildList(items: List):
    head = ListNode()
    if len(items):
        head.val = items[0]
    curr = head
    for idx in range(1, len(items)):
        curr.next = ListNode()
        curr = curr.next
        curr.val = items[idx]

    return head


for testCase in testCases:
    head = buildList(testCase["input"])
    runner = Solution(head)
    result = runner.getRandom()
    print(result)
