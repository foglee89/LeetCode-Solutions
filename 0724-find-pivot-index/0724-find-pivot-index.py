class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumL = 0
        
        for i, num in enumerate(nums):
            sumR = total - sumL - num
            if sumL == sumR:
                return i
            sumL += num
        
        return -1