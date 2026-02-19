# ==============================
# MIN COST CLIMBING STAIRS - ALL APPROACHES
# ==============================

# --------------------------------------------------
# Recursive Approach (Brute Force)
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        def solve(i):
            if i >= n:
                return 0
            return cost[i] + min(
                solve(i + 1),
                solve(i + 2)
            )
        return min(solve(0), solve(1))


# --------------------------------------------------
# Recursion + Memoization (Top-Down DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}
        def solve(i):
            if i >= n:
                return 0            
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(
                solve(i + 1),
                solve(i + 2)
            )
            return memo[i]
        return min(solve(0), solve(1))


# --------------------------------------------------
# Tabulation (Bottom-Up DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# --------------------------------------------------

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )
        return dp[n]


# --------------------------------------------------
# Space Optimized DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        prev2 = 0   # dp[i-2]
        prev1 = 0   # dp[i-1]
        for i in range(2, n + 1):
            current = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )
            prev2 = prev1
            prev1 = current
        return prev1
