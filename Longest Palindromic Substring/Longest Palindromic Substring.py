class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None

        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        start = None
        end = None
        for i, char in enumerate(s):
            if last_occurrence[char] != i:
                start = i
                end = last_occurrence[char]
                break

        if start is not None and end is not None:
            return s[start:end + 1]
        else:
            return s[0]


