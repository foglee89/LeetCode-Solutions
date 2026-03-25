class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        counts_ransom = collections.Counter(ransomNote)
        counts_magazine = collections.Counter(magazine)

        for ch, cnt in counts_ransom.items():
            if ch not in counts_magazine or counts_magazine[ch] < cnt:
                return False
        
        return True