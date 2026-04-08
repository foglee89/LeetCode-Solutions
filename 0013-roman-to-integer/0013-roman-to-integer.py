class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot = 0
        l = len(s)-1
        for i in range(l, -1, -1):
            r = s[i]
            
            if i < l and romanDict[r] < romanDict[s[i+1]]:
                tot -= romanDict[r]
            else:
                tot += romanDict[r]
        
        return tot
