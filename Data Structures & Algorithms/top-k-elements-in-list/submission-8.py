class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # minheap
        heap = []
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for j in d:
            heapq.heappush(heap, (d[j], j))
        while len(heap) > k:
            heapq.heappop(heap)
        return [i[1] for i in heap]
        
        
