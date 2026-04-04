class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        available = {}

        for i,n in enumerate(nums):
            if n not in available:
                available[n] = i

            t = target-n
            
            if t in available and available[t] != i:
                return [available[t], i]
                # ti = available[t][0]
                # if len(available[t]) == 2:
                #     return available[t]
                # elif ti == i:
                #     continue
                # else:
                #     return [i, ti]