class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for s, d, t in times:
            edges[s].append((d, t))

        minHeap = [(0, k)]
        durations = {}
        tt = 0

        while minHeap:
            
            t1, n1 = heapq.heappop(minHeap)

            if n1 not in durations:
                durations[n1] = t1
                tt = t1

                for n2, t2 in edges[n1]:
                    heapq.heappush(minHeap, (t1+t2, n2))

        return -1 if len(durations) < n else tt