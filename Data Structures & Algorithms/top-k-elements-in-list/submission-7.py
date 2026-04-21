class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: num, value: frequency -> swap key and value pair -> sort
        d = defaultdict(int)
        tmp = []
        for i in nums:
            d[i] += 1
        for j in d:
            tmp.append((d[j], j))
        tmp.sort()
        res = []
        while len(res) < k:
            res.append(tmp.pop()[1])
        return res
