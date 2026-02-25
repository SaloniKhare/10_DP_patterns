``` python
class SpaceOptimizedSolution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        # Start from last row
        prev = triangle[n - 1][:]
        for i in range(n - 2, -1, -1):
            current = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                current[j] = triangle[i][j] + min(
                    prev[j],
                    prev[j + 1]
                )
            prev = current
        return prev[0]
```
