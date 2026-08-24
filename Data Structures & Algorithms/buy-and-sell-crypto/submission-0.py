
"""
[10,1,5,6,7,1]
    l       r

if prices[r] < prices[l]:
while r < len(prices) - 1:
    r = +=1
    while prices[r] < prices[l]:
        l += 1
    
    res = max(res, prices[r] - prices[l])




"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(prices) - 1:
            r +=1
            while prices[r] < prices[l]:
                l += 1
            
            res = max(res, prices[r] - prices[l])
        return res