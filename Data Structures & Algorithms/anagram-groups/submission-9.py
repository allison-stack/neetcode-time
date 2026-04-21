class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: sorted anagram, value: [anagrams]
        d = defaultdict(list)
        for i in strs:
            d["".join(sorted(i))].append(i)
        return [i for i in d.values()]