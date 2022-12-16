"""
Question: https://leetcode.com/problems/search-insert-position
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftPointer, rightPointer = 0, len(nums)-1

        while leftPointer <= rightPointer:
            midPointer = leftPointer + (rightPointer - leftPointer) // 2
            if target == nums[midPointer]:
                return midPointer
            if target < nums[midPointer]:
                rightPointer = midPointer-1
            if target > nums[midPointer]:
                leftPointer = midPointer+1

        return midPointer if nums[midPointer] > target else midPointer+1


testCases = [
    {
        "nums":  [1, 3, 5, 6],
        "target": 5,
        "output": 2
    },
    {
        "nums":  [1, 3, 5, 6],
        "target": 2,
        "output": 1
    },
    {
        "nums":  [1, 3, 5, 6],
        "target": 7,
        "output": 4
    },
    {
        "nums": [1, 3, 5, 6],
        "target": 0,
        "output": 0
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.searchInsert(testCase["nums"], testCase["target"])
    print(result)
