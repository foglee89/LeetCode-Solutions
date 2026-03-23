class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if c in brackets and stack:
                if stack.pop() != brackets[c]:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
