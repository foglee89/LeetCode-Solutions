class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumL = 0
        
        for i in range(len(nums)):
            sumR = total - (sumL+ nums[i])
            if sumL == sumR:
                return i
            sumL += nums[i]
        
        return -1