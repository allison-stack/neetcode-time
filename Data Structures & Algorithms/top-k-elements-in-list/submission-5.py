class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        a = []
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in d:
            a.append((d[j], j))
        a.sort()
        a.reverse()
        for l in a[:k]:
            res.append(l[1])
        return res

        