class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n > len(haystack):
            return -1

        for i, c in enumerate(haystack):

            if haystack[i:i+n] == needle:
                return i
        return -1
