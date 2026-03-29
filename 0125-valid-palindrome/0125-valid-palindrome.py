class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            print(L, s[L], R, s[R])
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            elif s[L].lower() != s[R].lower():
                return False
            else:
                L += 1
                R -= 1
        return True