"""
counter = {
    a: 0,
    b: 0,
    c: 0
}

lecabee
  l r

if s2[r] in counter:
    counter[s2[r]] -= 1

while (r - l + 1) > len(s1) or counter[s2[r]] < 0:
    if s2[l] in counter:
        counter[s2[l]] += 1
    l+=1

if max(counter.values()) == 0:
    return True


"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        counter = {}
        for c1 in s1:
            if c1 not in counter:
                counter[c1] = 0
            counter[c1] += 1
        
        for r in range(len(s2)):
            if s2[r] in counter:
                counter[s2[r]] -= 1
            
            while (r - l + 1) > len(s1) or counter.get(s2[r], 0) < 0:
                if s2[l] in counter:
                    counter[s2[l]] += 1
                l += 1
            
            if max(counter.values()) == 0:
                return True
        
        return False
        
