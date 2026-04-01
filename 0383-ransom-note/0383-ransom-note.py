class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        magLetters = collections.Counter(magazine)
        
        for c in ransomNote:
            if magLetters[c] <= 0:
                return False
            
            magLetters[c] -= 1
        return True
