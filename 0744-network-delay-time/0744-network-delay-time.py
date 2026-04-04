class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for s, d, t in times:
            edges[s].append((d, t))

        shortest = {}
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            shortest[n1] = t1
            t = t1

            for n2, t2 in edges[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t1+t2, n2))

        return -1 if len(shortest) < n else t