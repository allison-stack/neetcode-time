class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort (frequency map)
        count = defaultdict(int)
        # frequencies 1 to len(nums)
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for i in nums:
            count[i] += 1
        for j in count:
            freq[count[j]].append(j)
        # append top frequent elements to result
        for l in range(len(freq)-1, 0, -1):
            for num in freq[l]:
                res.append(num)
                if len(res) == k:
                    return res


        

        
        
