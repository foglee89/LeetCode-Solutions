class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_counts = collections.Counter(t)
        s_counts = collections.Counter(s)

        if t_counts != s_counts:
            return False
        else:
            return True
        
        # for c in s:
        #     if c not in t_counts:
        #         return False
        #     elif t_counts[c] <= 0:
        #         return False
        #     else:
        #         t_counts[c] -= 1
        
        # for v in 