"""
Question: https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        res = strs[0]
        for i in range(1, len(strs)):
            curr = strs[i]
            for j in range(len(res)):
                if res[j] != curr[j]:
                    res = res[:j]
                    if res == '':
                        return res
                    else:
                        break
        return res


test_cases = [{
    "strs": ["flower", "flow", "flight"],
    "output": "fl"
}, {
    "strs": ["dog", "racecar", "car"],
    "output": ""
}]

for test_case in test_cases:
    runner = Solution()
    print(runner.longestCommonPrefix(test_case["strs"]))
