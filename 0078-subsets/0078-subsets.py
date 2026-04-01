class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]

        # for num in nums:
        #     res += [subset + [num] for subset in res]
        # return res

        curSet, subsets = [], []
        self.helperUnique(0, nums, curSet, subsets)
        return subsets

    def helperUnique(self, i, nums, curSet, subsets):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return

        # inc nums[i]
        curSet.append(nums[i])
        self.helperUnique(i+1, nums, curSet, subsets)
        curSet.pop()

        # not inc nums[i]
        self.helperUnique(i+1, nums, curSet, subsets)