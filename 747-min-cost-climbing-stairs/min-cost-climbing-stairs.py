class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0]*len(cost)
        if n == 1:
            return cost[0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = min(dp[i-1]+ cost[i],dp[i-2]+cost[i])
        print(dp)
        return min(dp[-1], dp[-2])           


        