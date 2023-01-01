"""
Question: https://leetcode.com/problems/find-the-k-beauty-of-a-number/
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        result = 0
        digitString = str(num)
        for i in range(len(digitString) - k + 1):
            currSubstring = int(digitString[i:i+k])
            # print("currSubstring: ", currSubstring)
            if currSubstring != 0 and num % currSubstring == 0:
                result += 1

        return result


testCases = [
    {
        "num": 240,
        "k":  2,
        "output": 2
    },
    {
        "num": 430043,
        "k":  2,
        "output": 2
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.divisorSubstrings(testCase["num"], testCase["k"])
    print(result)
