class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def helper(i, curComb):
            if len(curComb) == k:
                combinations.append(curComb.copy())
                return
            if i > n:
                return
            # sub-optimal backtracking
            # # to inc i
            # curComb.append(i)
            # helper(i+1, curComb)
            # curComb.pop()

            # # not inc i
            # helper(i+1, curComb)

            # optimal backtracking

            for j in range(i, n+1):
                curComb.append(j)
                helper(j+1, curComb)
                curComb.pop()

        helper(1, [])
        return combinations
