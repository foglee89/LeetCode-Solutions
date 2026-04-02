class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.helper(1, [], combinations, n, k)
        return combinations

    def helper(self, i, curComb, combinations, n, k):
        if len(curComb) == k:
            combinations.append(curComb.copy())
            return
        if i > n:
            return

        # to inc i
        curComb.append(i)
        self.helper(i+1, curComb, combinations, n, k)
        curComb.pop()

        # not inc i
        self.helper(i+1, curComb, combinations, n, k)

        # def helper(i, curComb):
        #     if len(curComb) == k:
        #         combinations.append(curComb)
        #         return
        #     if i > n:
        #         return

        #     # to inc i
        #     curComb.append(i)
        #     helper(i+1, curComb)
        #     curComb.pop()

        #     # not inc i
        #     helper(i+1, curComb)

        # helper(1, [])
        # return combinations

