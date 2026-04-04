class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        available = collections.defaultdict(list)
        for i, n in enumerate(nums):
            available[n].append(i)

        for i,n in enumerate(nums):
            t = target-n
            
            if t in available:
                ti = available[t][0]
                if len(available[t]) == 2:
                    return available[t]
                elif ti == i:
                    continue
                else:
                    return [i, ti]