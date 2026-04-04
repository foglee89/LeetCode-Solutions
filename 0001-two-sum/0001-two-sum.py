class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        available = {}
        for i, n in enumerate(nums):
            available[i] = n

        for i,n in enumerate(nums):
            t = target-n
            keys = [k for k, v in available.items() if v == t]
            if len(keys) == 2:
                return keys
            if keys and keys[0] != i:
                return [i, keys[0]]