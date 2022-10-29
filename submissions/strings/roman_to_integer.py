"""
Question: https://leetcode.com/problems/roman-to-integer/
"""


class Solution:

    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s_len = len(s)
        res = 0
        prev = ''
        for idx in range(s_len - 1, -1, -1):
            if s[idx] == 'I' and (prev == 'V' or prev == 'X'):
                res -= 1
            elif s[idx] == 'C' and (prev == 'D' or prev == 'M'):
                res -= 100
            elif s[idx] == 'X' and (prev == 'L' or prev == 'C'):
                res -= 10
            else:
                res += dict[s[idx]]
            prev = s[idx]
        return res


test_cases = [{
    "s": "III",
    "output": 3
}, {
    "s": "LVIII",
    "output": 58
}, {
    "s": "MCMXCIV",
    "output": 1994
}]

for test_case in test_cases:
    runner = Solution()
    print(runner.romanToInt(test_case["s"]))
