from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        maxProfit = -999999
        profit = 0

        if len(prices) == 1:
            return 0
        
        while rp <= len(prices) - 1:
            if prices[lp] < prices[rp]:
                profit = prices[rp] - prices[lp]
                maxProfit = max(profit, maxProfit)
            # if the left price is bigger then move the next pointer
            else:
               lp = rp
            rp += 1
            
        if maxProfit < 0:
            return 0
        return maxProfit
    
s = Solution()

prices = [1,2,4]


print(s.maxProfit(prices))