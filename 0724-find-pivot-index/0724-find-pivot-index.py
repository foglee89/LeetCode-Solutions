class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSums = [0]*(n+1)
        for i in range(n):
            preSums[i+1] = preSums[i] + nums[i]
        
        for i in range(n):
            sumL = preSums[i]
            sumR = preSums[n] - preSums[i+1]
            if sumL == sumR:
                return i
        
        return -1