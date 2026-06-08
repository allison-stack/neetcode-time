class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input: grid (0 water, 1 island)
        # output: find number of islands
        # one island includes connecting adjacent lands
        # min grid length -> 1
        # water is surrounding grid
        # ======
        # 1. traverse through grid
            # if curr element is 1, DFS - mark visited as 0
            # +1 island
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(r,c):
            # base case
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
                return
            # sink curr visited land piece
            grid[r][c]="0"
            # dfs traversal
            for x,y in directions:
                dfs(r+x, c+y)
        # traverse through grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    # DFS
                    dfs(r,c)
                    islands+=1
        return islands

        


        