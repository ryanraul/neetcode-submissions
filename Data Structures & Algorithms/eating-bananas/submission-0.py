"""

If each pile needs 1 hour
k = Bananas per hour is = Bananas per pile
total_time => sum(pile => math.ceil(pile.totalBananas / k))

h is the total hours to eat all the bananas
if total_time > h:
    increase k which is the division rate
else:
    save k because it is one of the response candidates
    reduces the k
    we need to get the minimum valid rate


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res





