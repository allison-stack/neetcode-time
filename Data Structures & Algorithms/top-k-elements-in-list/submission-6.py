class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        heap = []
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in d:
            heapq.heappush(heap, (d[j], j))
            if len(heap) > k:
                heapq.heappop(heap)
        for l in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

        