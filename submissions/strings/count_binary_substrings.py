"""
Question: https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
	def countBinarySubstrings(self, s: str) -> int:
		cnt_list = []

		prev = s[0]
		cnt = 1
		for idx in range(1, len(s)):
			if prev == s[idx]:
				cnt += 1
			else:
				cnt_list.append(cnt)
				cnt = 1
				prev = s[idx]
		cnt_list.append(cnt)
		
		res = 0
		for idx in range(1, len(cnt_list)):
			res += min(cnt_list[idx - 1], cnt_list[idx])

		return res


test_cases = [{"s": "00110011", "output": 6}, {"s": "10101", "output": 4}]

for test_case in test_cases:
	runner = Solution()
	print(runner.countBinarySubstrings(test_case["s"]))
