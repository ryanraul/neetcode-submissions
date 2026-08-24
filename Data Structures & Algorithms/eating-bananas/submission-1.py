
"""
piles with bananas
h - total hours to eat all bananas
k - bananas eat per hour

res = minimum k valid

the minimum valu k could be is 1
the maximum value k could be the greatest value in piles
1 <= k <= max(piles)

total_hours = piles.sum(p => p/k)
total_hours > h:
    increase k to get lower values
else:
    res = min(res, k)
    decrease k to try to get the minimum k valid

[1,4,3,2]
h=9

l = 1
r = 4
k = 2

[1,4,3,2]
[1+2+2+1] = 6

6 < 9
    res = min(4,2) = 2
    r = 2 - 1 = 1

l = 1
r = 1
k = 1


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r
        while l <= r:
            k = (l+r)//2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/k)
            
            if total_hours > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
            
        return res

