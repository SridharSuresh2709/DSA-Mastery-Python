class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        minprice = float('inf')
        for i in range(0,len(prices)):
            minprice = min(minprice,prices[i])
            profit = prices[i]-minprice
            maxprofit = max(maxprofit , profit)
        return maxprofit
