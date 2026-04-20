class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers problem
        l, r = 0, len(heights)-1
        m = 0
        while l < r:
            # width is calulcated by (l-r)
            m = max(m, min(heights[l], heights[r])*(r-l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] >= heights[l]:
                l += 1
        return m
                
                
        