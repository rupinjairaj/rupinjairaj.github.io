"""
Question: https://leetcode.com/problems/contains-duplicate-ii/
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elementToIdx = dict()

        for i in range(len(nums)):
            if nums[i] not in elementToIdx:
                elementToIdx[nums[i]] = i
            else:
                if i - elementToIdx[nums[i]] <= k:
                    return True
                else:
                    elementToIdx[nums[i]] = i
        return False


testCases = [
    {
        "nums": [1, 2, 3, 1],
        "k": 3,
        "output": True
    },
    {
        "nums": [1, 0, 1, 1],
        "k": 1,
        "output": True
    },
    {
        "nums": [1, 2, 3, 1, 2, 3],
        "k": 2,
        "output": False
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.containsNearbyDuplicate(testCase["nums"], testCase["k"])
    print(result)
