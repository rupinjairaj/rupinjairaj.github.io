"""
Question: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""
from typing import List
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixSums = []
        currSum = 0
        for num in nums:
            currSum += num
            prefixSums.append(currSum)

        answer = []
        for query in queries:
            i = bisect.bisect(prefixSums, query)
            answer.append(i)

        return answer


testCases = [
    {
        "nums": [4, 5, 2, 1],
        "queries":  [3, 10, 21],
        "output": [2, 3, 4]
    },
    {
        "nums": [2, 3, 4, 5],
        "queries":  [1],
        "output": [0]
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.answerQueries(testCase["nums"], testCase["queries"])
    print(result)
