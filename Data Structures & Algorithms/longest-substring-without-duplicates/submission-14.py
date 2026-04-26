class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window question
        l, r = 0, 0
        seen = {}
        res = 0
        for i in range(len(s)):
            if s[i] in seen:
                # adjust right point to point to index of seen element + 1
                l = max(seen[s[i]] + 1, l)
                seen.pop(s[i])
            seen[s[i]] = i 
            res = max(res, r-l+1)
            r += 1
        return res

        