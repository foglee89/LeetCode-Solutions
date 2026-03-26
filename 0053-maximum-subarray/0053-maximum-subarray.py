class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set a curr/max sum to ref and my L pointer
        maxSum = nums[0] #-float("inf")
        currSum = 0

        # # iter through the arr
        # for R in range(len(nums)):
            
        #     # recalc currSum and check if larger than maxSum
        #     currSum += nums[R]
        #     # if larger, update maxSum and progress
        #     maxSum = max(maxSum, currSum)

        #     # if smaller, update currSum and L
        #     if currSum < maxSum:
        #         currSum -= nums[L]
        #         L += 1

        for num in nums:
            currSum = max(currSum, 0) + num
            maxSum = max(maxSum, currSum)
        
        return maxSum
