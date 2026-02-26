``` python
class RecursionSolution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        def helper(i, j):
            # Out of bounds
            if j < 0 or j >= n:
                return float('inf')
            # Last row
            if i == n - 1:
                return matrix[i][j]
            down = helper(i + 1, j)
            left_diag = helper(i + 1, j - 1)
            right_diag = helper(i + 1, j + 1)
            return matrix[i][j] + min(down, left_diag, right_diag)
        result = float('inf')
        for col in range(n):
            result = min(result, helper(0, col))
        return result
```
