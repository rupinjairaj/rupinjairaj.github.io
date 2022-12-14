"""
Question: https://leetcode.com/problems/palindrome-number/description/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x_string = str(x)

        return x_string == x_string[::-1]


testCases = [
    {
        "x": 121,
        "output": True
    },
    {
        "x": -121,
        "output": False
    },
    {
        "x": 10,
        "output": False
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.isPalindrome(testCase["x"])
    print(result)
