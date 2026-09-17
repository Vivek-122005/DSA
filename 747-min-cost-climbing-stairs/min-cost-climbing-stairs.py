class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0]*3
        print(dp)
        if n == 1:
            return cost[0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[2] = cost[i] + min(dp[1],dp[0])
            dp[0] = dp[1]
            dp[1] = dp[2]
        return min(dp[1], dp[0])           


        