"""
Question: https://leetcode.com/problems/length-of-last-word/
"""
class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		s_list = s.split(" ")
		for ele in range(len(s_list) - 1, -1, -1):
			if s_list[ele] != "":
				return len(s_list[ele])


test_cases = [
	{"s": "Hello World", "output": 5},
	{"s": "   fly me   to   the moon  ", "output": 4},
	{"s": "luffy is still joyboy", "output": 6},
]

for test_case in test_cases:
	runner = Solution()
	print(runner.lengthOfLastWord(test_case["s"]))
