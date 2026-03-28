class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ci = 2

        for i in range(2, len(nums)):

            if nums[i] != nums[ci-1]:
                nums[ci] = nums[i]
                ci += 1

            elif nums[i] != nums[ci-2]:
                nums[ci] = nums[i]
                ci += 1

        return ci