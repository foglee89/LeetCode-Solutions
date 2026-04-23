class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        freq = sorted(freq, key=lambda cnt: freq[cnt], reverse='True')

        res = []

        for i in range(k):
            res.append(freq[i])

        return res
            

        # for num, cnt in numCount.items():
        #     freq[cnt].append(num)
        # for i in range(len(freq)-1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res

            