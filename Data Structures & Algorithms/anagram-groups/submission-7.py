class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(List)
        ans = []
        for i in strs:
            if str(sorted(i)) not in d:
                d[str(sorted(i))] = [i]
            else:
                d[str(sorted(i))].append(i)
        for j in d.values():
            ans.append(j)
        return ans
        