class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        counts_magazine = collections.Counter(magazine)

        for ch in ransomNote:
            if counts_magazine[ch] <= 0:
                return False
            
            counts_magazine[ch] -= 1
        
        return True