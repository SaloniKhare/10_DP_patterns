``` python
class SpaceOptimizedSolution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        prev = matrix[0][:]
        for i in range(1, n):
            current = [0] * n
            for j in range(n):
                up = prev[j]
                left_diag = prev[j - 1] if j > 0 else float('inf')
                right_diag = prev[j + 1] if j < n - 1 else float('inf')
                current[j] = matrix[i][j] + min(up, left_diag, right_diag)
            prev = current
        return min(prev)
```
