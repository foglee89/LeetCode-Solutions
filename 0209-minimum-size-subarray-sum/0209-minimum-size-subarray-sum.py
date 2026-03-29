class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curLen = float('inf')
        curSum, L = 0, 0

        for R in range(len(nums)):
            curSum += nums[R]

            while curSum >= target:
                curLen = min(curLen, R-L+1)
                curSum -= nums[L]
                L += 1

        return 0 if curLen == float('inf') else curLen