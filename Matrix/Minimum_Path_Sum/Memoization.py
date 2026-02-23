``` python
class MemoizationSolution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def helper(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            right = helper(i, j + 1)
            down = helper(i + 1, j)
            memo[(i, j)] = grid[i][j] + min(right, down)
            return memo[(i, j)]
        return helper(0, 0)
```
