class Solution:
    def longestPalindrome(self, s: str) -> str:
        stIdx, length = 0,0

        for i in range(len(s)):

            odd = self.helper(s, i, i)
            stIdx = stIdx if length > odd[1] else odd[0]
            length = length if length > odd[1] else odd[1]

            even = self.helper(s, i, i+1)
            stIdx = stIdx if length > even[1] else even[0]
            length = length if length > even[1] else even[1]

        return s[stIdx : stIdx + length]

    def helper(self, s, l, r) -> tuple:
        stIdx, maxLen = 0, 0
        while l >= 0 and r < len(s) and s[l]==s[r]:
            if r-l+1 > maxLen:
                stIdx = l
                maxLen = r-l+1

            l -= 1
            r += 1

        return stIdx, maxLen