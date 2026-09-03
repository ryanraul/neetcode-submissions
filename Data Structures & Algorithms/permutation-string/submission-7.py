"""
using sliding window

s1 = "abc" 
s2 = "lecabee"
        l
          r

    
while r < len(s2):
    while (r - l + 1) > len(s1) or counter[s[r]] < 0:
        if s[l] in counter:
            counter[s[l]] += 1
        l += 1
    
        if the biggest value in counter is zero, it means that we found a permutation:
            return true

        if l > r:
            r = l

    return false
    

counter_s1 =
{
    a: 1,
    b: 1,
    c: 1
}

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        counter = {}

        for c in s1:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        
        while r < len(s2):

            if s2[r] in counter:
                counter[s2[r]] -= 1
            
            while (r - l + 1) > len(s1) or counter.get(s2[r], 0) < 0:
                if s2[l] in counter:
                    counter[s2[l]] += 1
                l += 1

            if max(counter.values()) == 0:
                return True        

            r += 1

        return False
