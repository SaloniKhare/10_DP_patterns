``` pyhton
class RecursionSolution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        def helper(i, j):
            # If out of bounds → return large value
            if i >= m or j >= n:
                return float('inf')
            # If destination reached
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            # Move right and down
            right = helper(i, j + 1)
            down = helper(i + 1, j)
            return grid[i][j] + min(right, down)
        return helper(0, 0)

```
