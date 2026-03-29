class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_counts = collections.Counter(nums)
        n = len(nums)

        for ele, count in ele_counts.items():
            if count > (n/2):
                return ele