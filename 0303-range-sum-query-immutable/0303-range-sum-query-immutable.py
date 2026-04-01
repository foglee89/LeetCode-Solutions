class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        tot = 0
        for n in nums:
            tot += n
            self.sums.append(tot)
            

    def sumRange(self, left: int, right: int) -> int:
        sumL = self.sums[left-1] if left > 0 else 0
        return self.sums[right]-sumL
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)