#121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        minval=max(prices)
        for i in prices:
           #get current maximum
           #get all the minimums prior to that
            if(i<minval):
                minval=i
            if(i-minval>profit):
                profit=i-minval
        return profit
