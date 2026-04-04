class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        available = {}

        for i,n in enumerate(nums):
            if n not in available:
                available[n] = i
            
            if target-n in available and available[target-n] != i:
                return [available[target-n], i]
