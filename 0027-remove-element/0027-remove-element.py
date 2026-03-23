class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ci = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[ci] = nums[i]
                ci += 1
        
        return ci
