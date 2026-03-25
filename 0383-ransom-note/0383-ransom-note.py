class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts_ransom = collections.Counter(ransomNote)
        counts_magazine = collections.Counter(magazine)

        for c in counts_ransom:
            if c in counts_magazine:
                counts_ransom[c] -= counts_magazine[c]
        
        rem = 0

        for c in counts_ransom.values():
            if c > 0:
                rem +=1 
        
        if rem:
            return False
        else:
            return True