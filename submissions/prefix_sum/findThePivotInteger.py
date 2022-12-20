
"""
Question: https://leetcode.com/problems/find-the-pivot-integer/description/
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixSums = [0]

        i = 1
        while i <= n:
            prefixSums.append(prefixSums[-1]+i)
            i += 1

        for i in range(len(prefixSums)-2, -1, -1):
            if prefixSums[-1] - prefixSums[i] == prefixSums[i+1]:
                return i+1

        return -1


testCases = [
    {
        "n": 8,
        "output": 6
    },
    {
        "n": 1,
        "output": 1
    },
    {
        "n": 4,
        "output": -1
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.pivotInteger(testCase["n"])
    print(result)
