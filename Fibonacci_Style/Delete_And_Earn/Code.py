# ==============================
# DELETE AND EARN - ALL APPROACHES
# ==============================

# Problem:
# You are given an integer array nums.
# You can pick any number nums[i] and earn nums[i] points.
# But after picking nums[i], you must delete every element equal to
# nums[i] - 1 and nums[i] + 1.
# Return the maximum points you can earn.


from collections import Counter
class RecursionSolution:
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        unique_nums = sorted(count)
        def helper(index):
            if index >= len(unique_nums):
                return 0
            # Option 1: Skip current number
            skip = helper(index + 1)
            # Option 2: Take current number
            take = unique_nums[index] * count[unique_nums[index]]
            next_index = index + 1
            # If next number is consecutive, skip it
            if next_index < len(unique_nums) and \
               unique_nums[next_index] == unique_nums[index] + 1:
                next_index += 1
            take += helper(next_index)
            return max(skip, take)
        return helper(0)


class MemoizationSolution:
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        unique_nums = sorted(count)
        memo = {}
        def helper(index):
            if index >= len(unique_nums):
                return 0
            if index in memo:
                return memo[index]
            skip = helper(index + 1)
            take = unique_nums[index] * count[unique_nums[index]]
            next_index = index + 1
            if next_index < len(unique_nums) and \
               unique_nums[next_index] == unique_nums[index] + 1:
                next_index += 1
            take += helper(next_index)
            memo[index] = max(skip, take)
            return memo[index]
        return helper(0)


class TabulationSolution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        count = Counter(nums)
        max_num = max(nums)
        # Convert to House Robber style problem
        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]
        dp = [0] * (max_num + 1)
        dp[1] = points[1] if max_num >= 1 else 0
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        return dp[max_num]


class SpaceOptimizedSolution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        count = Counter(nums)
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]
        prev2 = 0
        prev1 = points[1] if max_num >= 1 else 0
        for i in range(2, max_num + 1):
            current = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = current
        return prev1
