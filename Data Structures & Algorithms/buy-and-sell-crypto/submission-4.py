"""
using two pointers
- left track buy prices
- right track sell prices

- left stays on the best day for buy new neet coins
- right keep trying to find a best day for buy

- for each iteration
    - if current price (right pointer) is less than current best day to buy (left pointer)
        - update the best day to buy with the right pointer
    - simulate a transaction with the current best buy day and currrent price (right pointer)
    - save the maximum result found
        - transation_price = prices[l] - prices[r]
        - result = max(transaction_price, result)

[10,1,5,6,7,1]
    l  
            r

[10,8,7,5,2]
          l
          r

[5,1,5,6,7,1,10]
   l
         r
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        best_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            best_profit = max(best_profit, prices[r] - prices[l])
            r += 1

        return best_profit