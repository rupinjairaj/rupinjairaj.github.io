"""
Question: https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split(" ")[1].isnumeric():
                digit_logs.append(log)
            else:
                log_elements = log.split(" ")
                letter_logs.append((log_elements[0], " ".join(log_elements[1:])))

        letter_logs.sort(key=lambda x: (x[1], x[0]))

        letter_logs = [" ".join([x, y]) for x, y in letter_logs]
        return letter_logs + digit_logs


test_cases = [
    {
        "logs": [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ],
        "output": [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
    },
    {
        "logs": [
            "a1 9 2 3 1",
            "g1 act car",
            "zo4 4 7",
            "ab1 off key dog",
            "a8 act zoo",
        ],
        "output": [
            "g1 act car",
            "a8 act zoo",
            "ab1 off key dog",
            "a1 9 2 3 1",
            "zo4 4 7",
        ],
    },
]

for test_case in test_cases:
    runner = Solution()
    print(runner.reorderLogFiles(test_case["logs"]))
