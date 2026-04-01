class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magLetters = collections.Counter(magazine)
        
        for c in ransomNote:
            if magLetters[c] <= 0:
                return False
            else:
                magLetters[c] -= 1
        return True
