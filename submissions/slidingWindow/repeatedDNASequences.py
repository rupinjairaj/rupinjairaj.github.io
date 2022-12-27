"""
Question: https://leetcode.com/problems/repeated-dna-sequences/
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        windowLength = 10
        previouslySeen = set()
        resultSet = set()
        for i in range(0, len(s)):
            currentSequence = s[i:i+windowLength]
            if currentSequence in previouslySeen:
                resultSet.add(currentSequence)
            else:
                previouslySeen.add(currentSequence)

        return resultSet


testCases = [
    {
        "s": "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "output": ["AAAAACCCCC", "CCCCCAAAAA"]
    },
    {
        "s": "AAAAAAAAAAAAA",
        "output": ["AAAAAAAAAA"]
    }
]


for testCase in testCases:
    runner = Solution()
    result = runner.findRepeatedDnaSequences(testCase["s"])
    print(result)
