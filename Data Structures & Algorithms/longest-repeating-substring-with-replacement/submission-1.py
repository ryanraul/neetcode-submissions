"""

AAABABB
l  r




while r < len(s):

    if s[r] not in counter:
        counter[s[r]] = 0
    counter[s[r]] += 1

    mostFreq = max(counter.values())
    length = r - l + 1

    while length - mostFreq > k:
        counter[s[l]] -= 1
        l+=1
    
    res = max(res, r - l + 1)


"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        counter = {}

        while r < len(s):
            if s[r] not in counter:
                counter[s[r]] = 0
            counter[s[r]] += 1

            while ((r - l + 1) - max(counter.values())) > k:
                counter[s[l]] -= 1
                l+=1
            
            res = max(res, r - l + 1)
            r += 1
        return res


