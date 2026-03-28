class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0

        for i in range(len(nums)):
            if i-1<0 or nums[i] != nums[i-1]:
                nums[c] = nums[i]
                c += 1
            
        return c