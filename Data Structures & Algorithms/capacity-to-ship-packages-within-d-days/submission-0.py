"""
days -> limit to shipped packages
weights -> ith is a package

return least weight capacity

worst cenario is we need max weight capacity
max is the sum of wall packages
minimum is greatest 1 package weight
how much weight per day


[1,5,4,4,2,3]
l = 5
r = 19

mid = 5 + 19 // 2 = 12

12 * 3 = 36
36 > 19
    r = 12 - 1
l = 5
r = 11
mid = (5 + 11) // 2 = 8

8 * 3 = 24
24 > 19
    r = 8 - 1

l = 5
r = 7
mid = (5+7) // 2 = 6

6 * 3 = 18
18 < 19
    l = 6 + 1

l = 7
r = 7

mid = (7+7) // 2 = 7
7 * 3 = 21


"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        res = r

        while l <= r:
            cap = (l+r)//2

            days_needed = 1 
            current_cap = cap
            for w in weights:
                if current_cap - w < 0:
                    days_needed += 1
                    current_cap = cap
                current_cap -= w
            
            if(days_needed > days):
                l = cap + 1
            else:
                res = min(cap, res)
                r = cap - 1
        return res
        