class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(lambda c: c.isalnum(), s)
        s = map(lambda c: c.lower(), s)
        s = list(s)
        s_rev = s[::-1]

        return s == s_rev
