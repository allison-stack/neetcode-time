class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        l, r = 0, 0
        seen = {}
        res = 0
        while r < len(s):
            if s[r] in seen:
                # set l to the next index after the last recorded index of seen element
                l = max(seen[s[r]]+1, l)
            # update seen index
            seen[s[r]] = r
            res = max(res, r-l+1)
            r += 1
        return res
            
        