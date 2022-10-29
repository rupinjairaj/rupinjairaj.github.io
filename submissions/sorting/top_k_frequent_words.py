"""
Question: https://leetcode.com/problems/top-k-frequent-words/
"""

from collections import defaultdict
from functools import cmp_to_key
from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dict = defaultdict(set)

        for word in words:
            if word not in dict:
                dict[word] = 0
            dict[word] += 1

        res = []
        for key, val in dict.items():
            res.append((key, val))

        res.sort(key=lambda x: (-x[1], x[0]))
        return [res[x][0] for x in range(k)]


test_cases = [
    {
        "words": ["i", "love", "leetcode", "i", "love", "coding"],
        "k": 2,
        "output": ["i", "love"],
    },
    {
        "words": [
            "the",
            "day",
            "is",
            "sunny",
            "the",
            "the",
            "the",
            "sunny",
            "is",
            "is",
        ],
        "k": 4,
        "output": ["the", "is", "sunny", "day"],
    },
]

for test_case in test_cases:
    runner = Solution()
    print(runner.topKFrequent(test_case["words"], test_case["k"]))
