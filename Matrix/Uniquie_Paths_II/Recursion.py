``` python
class RecursionSolution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def helper(i, j):
            # Out of bounds
            if i >= m or j >= n:
                return 0
            # Obstacle cell
            if obstacleGrid[i][j] == 1:
                return 0
            # Destination reached
            if i == m - 1 and j == n - 1:
                return 1
            return helper(i, j + 1) + helper(i + 1, j)
        return helper(0, 0)
```
