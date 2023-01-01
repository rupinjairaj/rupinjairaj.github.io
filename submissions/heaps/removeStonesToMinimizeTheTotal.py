"""
Question: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
"""
from typing import List
import heapq
import math


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [pile * -1 for pile in piles]
        heapq.heapify(piles)

        while k > 0:
            k -= 1
            item = heapq.heappop(piles)
            remove = math.ceil(item / 2)
            item += (remove * -1)
            heapq.heappush(piles, item)

        return sum(piles) * -1


testCases = [
    {
        "piles": [5, 4, 9],
        "k": 2,
        "output": 12
    },
    {
        "piles": [4, 3, 6, 7],
        "k": 3,
        "output": 12
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.minStoneSum(testCase["piles"], testCase["k"])
    print(result)
