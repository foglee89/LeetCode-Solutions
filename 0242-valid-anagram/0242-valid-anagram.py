class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # t_counts = collections.Counter(t)

        # fastest and straightforward if collections allowed
        countS = collections.Counter(s)
        countT = collections.Counter(t)

        return countS == countT

        # faster and straightforward
        # s_counts = collections.Counter(s)

        # if t_counts != s_counts:
        #     return False
        # else:
        #     return True
        

        # less mem, slower
        # for c in s:
        #     if c not in t_counts:
        #         return False
        #     elif t_counts[c] <= 0:
        #         return False
        #     else:
        #         t_counts[c] -= 1
        
        # for v in t_counts.values():
        #     if v != 0:
        #         return False
        
        # return True