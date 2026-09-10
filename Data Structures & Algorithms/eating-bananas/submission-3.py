"""
- using binary search
- we can set a minimum and maximum eating rate (bananas per hour)
    - and try to find a value between this min and max values (left and right)

- left = 1 banana per hour
- right = the biggest pile = max(piles)

- apply the binary search, get the middle eating rate
- check if its enough to eating all the piles
    - get the total hours by simulating the eating process with this middle rate 
    - if the total_hours is bigger than the available (h)
        - try to get a bigger rate
    - oterwhise
        - save the mininum value between current response and current rate
        - and try to get a lower value (we want the minimum eating rate)


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        response = r

        while l <= r:
            mid_rate = (l+r) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/mid_rate)
            
            if total_hours > h:
                l = mid_rate + 1
            else:
                response = min(mid_rate, response)
                r = mid_rate - 1
            
        return response