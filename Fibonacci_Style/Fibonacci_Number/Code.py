```python
# ==============================
# FIBONACCI NUMBER - ALL APPROACHES
# ==============================

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]

            memo[n] = solve(n - 1) + solve(n - 2)
            return memo[n]

        return solve(n)


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
```
