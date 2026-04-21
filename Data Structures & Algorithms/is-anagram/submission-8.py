class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = defaultdict(int)
        d_t = defaultdict(int)
        for i in s:
            d_s[i] += 1
        for j in t:
            d_t[j] += 1
        return d_s == d_t