class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # optimized recursive
        # def helper(i):
        #     if i == len(nums):
        #         return [[]]

        #     resPerms = []
        #     perms = helper(i+1)
        #     for p in perms:
        #         for j in range(len(p)+1):
        #             pCopy = p.copy()
        #             pCopy.insert(j, nums[i])
        #             resPerms.append(pCopy)
        #     return resPerms


        # res = helper(0)
        # return res

        # iterative 
        perms = [[]]
        
        for n in nums:
            curPerm = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    curPerm.append(pCopy)
                perms = curPerm
        return perms