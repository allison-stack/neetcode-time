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
        map={}
        while right < len(s):
            if s[right] in map:
                left=max(left,map[s[right]]+1)
            map[s[right]]=right
            res=max(res,right-left+1)
            right+=1
        return res
            