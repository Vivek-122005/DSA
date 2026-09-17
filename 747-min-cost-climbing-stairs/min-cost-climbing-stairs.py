class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        index1 = 0
        index2 = 0
        curr = 0
        # print(dp)
        if n == 1:
            return cost[0]
        index1 = cost[0]
        index2 = cost[1]
        for i in range(2,n):
            curr = cost[i] + min(index1,index2)
            index1 = index2
            index2 = curr
        return min(index1, index2)           


        