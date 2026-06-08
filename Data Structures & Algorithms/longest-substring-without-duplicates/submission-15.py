class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: string
        # output: lenth of longest substring without duplicate characters
        # sliding window 
        # hash map
        # ======
        # go through string, check if curr is in hash map, if not add, if yes then shift left pointer, take max length at each step
        left,right=0,0
        res=0
        seen=set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            res=max(res,right-left+1)
            right+=1
        return res
            