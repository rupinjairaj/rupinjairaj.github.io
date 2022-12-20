"""
Question: https://leetcode.com/problems/find-the-highest-altitude/
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currAltitude = 0
        for altitudeGain in gain:
            currAltitude += altitudeGain
            maxAltitude = max(maxAltitude, currAltitude)

        return maxAltitude


testCases = [
    {
        "gain": [-5, 1, 5, 0, -7],
        "output": 1
    },
    {
        "gain": [-4, -3, -2, -1, 4, 3, 2],
        "output": 0
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.largestAltitude(testCase["gain"])
    print(result)
