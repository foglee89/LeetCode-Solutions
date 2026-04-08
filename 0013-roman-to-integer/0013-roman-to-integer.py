class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot = 0
        l = len(s)-1
        for i, r in enumerate(s):
            
            if r == 'I' and i < l and (s[i+1] == 'V' or s[i+1] == 'X'):
                tot -= romanDict[r]
            elif r == 'X' and i < l and (s[i+1] == 'L' or s[i+1] == 'C'):
                tot -= romanDict[r]
            elif r == 'C' and i < l and (s[i+1] == 'D' or s[i+1] == 'M'):
                tot -= romanDict[r]
            else:
                tot += romanDict[r]
        
        return tot
