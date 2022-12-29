"""
Question: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"""
from typing import List
import sys


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        result = sys.maxsize
        for idx in range(len(nums) - k + 1):
            result = min(result, nums[idx+k-1] - nums[idx])

        return result


testCases = [
    {
        "nums": [90],
        "k": 1,
        "output": 0
    },
    {
        "nums": [9, 4, 1, 7],
        "k": 2,
        "output": 2
    },
    {
        "nums": [41900, 69441, 94407, 37498, 20299, 10856, 36221, 2231, 54526, 79072, 84309, 76765, 92282, 13401, 44698, 17586, 98455, 47895, 98889, 65298, 32271, 23801, 83153, 12186, 7453, 79460, 67209, 54576, 87785, 47738, 40750, 31265, 77990, 93502, 50364, 75098, 11712, 80013, 24193, 35209, 56300, 85735, 3590, 24858, 6780, 50086, 87549, 7413, 90444, 12284, 44970, 39274, 81201, 43353, 75808, 14508, 17389, 10313, 90055, 43102, 18659, 20802, 70315, 48843, 12273, 78876, 36638, 17051, 20478],
        "k": 5,
        "output": 1428
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.minimumDifference(testCase["nums"], testCase["k"])
    print(result)
