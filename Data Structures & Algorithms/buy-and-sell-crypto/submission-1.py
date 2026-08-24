"""
[10,1,5,6,7,1]
    l
            r

[7,1,5,3,6,4]
   l r 

 if prices[r] < prices[l]
    l = r
 else:
    res = max(res, prices[l] - prices[r])
    r += 1

"""



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res


