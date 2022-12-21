"""
Question: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
"""

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        store = set()
        for num in range(left, right+1):
            store.add(num)

        for l, r in ranges:
            for i in range(l, r+1):
                if i in store:
                    store.remove(i)

        return len(store) == 0


class Solution2:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for num in range(left, right+1):
            for l, r in ranges:
                if l <= num <= r:
                    break
                else:
                    return False
        return True


testCases = [
    {
        "ranges": [[1, 2], [3, 4], [5, 6]],
        "left": 2,
        "right": 5,
        "output": True
    },
    {
        "ranges": [[1, 10], [10, 20]],
        "left": 21,
        "right":21,
        "output": False
    }
]

for testCase in testCases:
    runner = Solution2()
    result = runner.isCovered(
        testCase["ranges"], testCase["left"], testCase["right"])
    print(result)
