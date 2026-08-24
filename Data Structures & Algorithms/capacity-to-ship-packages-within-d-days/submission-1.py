"""
weights 

minimum cap possible is max(weights)
maximum cap possible is sum(weights)

max(weights) <= cap <= sum(weights)
binary search

with capacity = x how much days we need?
if days_needed > days
    we need to increase the capacity
else:
    we have a candidate for the response
    and we can try to decrease the capacity
    to get the minimum ship capacity possible

l = max(weights)
r = sum(weights)

res = r

[1,2,3,4,5]
l = 1
r = 15

15//2 = 7
[2]
dn = 3

3 < 5
res = min(15, 7) = 7
r = cap - 1 = 6

6+1 = 7
7//2 = 3

[5]
dn = 5




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
                if (current_cap - w) < 0:
                    days_needed += 1
                    current_cap = cap
                current_cap -= w
            
            if days_needed > days:
                l = cap + 1
            else:
                res = min(res, cap)
                r = cap - 1
            
        return res




        