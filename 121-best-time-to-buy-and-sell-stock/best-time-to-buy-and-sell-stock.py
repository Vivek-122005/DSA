class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        pro =0 
        N = len(prices)
        for i in range(N):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > pro:
                pro = prices[i] - buy
        return pro
        