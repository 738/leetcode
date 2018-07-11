class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                res.append(self.dfs(grid, i, j))
        return max(res)
    
    def dfs(self, grid, i, j):
        n,m=len(grid),len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        if (0 <= i < n and 0 <= j < m) and grid[i][j]:
            grid[i][j], neighbor = 0, 0
            for d in directions:
                neighbor += self.dfs(grid, i+d[0], j+d[1])
            return neighbor + 1
        else: return 0