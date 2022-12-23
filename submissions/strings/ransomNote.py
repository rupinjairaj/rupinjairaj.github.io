"""
Question: https://leetcode.com/problems/ransom-note/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNoteLetters = [0]*26
        for c in ransomNote:
            ransomNoteLetters[ord(c) - ord('a')] += 1

        magazineLetters = [0]*26
        for c in magazine:
            magazineLetters[ord(c) - ord('a')] += 1

        for idx in range(26):
            if ransomNoteLetters[idx] > 0 and ransomNoteLetters[idx] > magazineLetters[idx]:
                return False
        return True


testCases = [
    {
        "ransomNote":  "a",
        "magazine": "b",
        "output": False
    },
    {
        "ransomNote":  "aa",
        "magazine": "ab",
        "output": False
    },
    {
        "ransomNote":  "aa",
        "magazine": "aab",
        "output": True
    }
]

for testCase in testCases:
    runner = Solution()
    result = runner.canConstruct(testCase["ransomNote"], testCase["magazine"])
    print(result)
