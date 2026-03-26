class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        currSum, L = 0, 0

        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                minLen = min(minLen, R-L+1)
                currSum -= nums[L]
                L += 1
        
        return 0 if minLen == float("inf") else minLen