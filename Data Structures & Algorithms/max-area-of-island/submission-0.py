class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            for x,y in directions:
                area+=dfs(r+x,c+y)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    max_area=max(max_area,area)
        return max_area
        