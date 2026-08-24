"""
"lecabee"
"abc"

{
    a: 0
    b: 0
    c: 0
}
"lecabee"
   l  r

 if s[r] in counter:
    counter[s[r]] -= 1

 while (r - l + 1) > len(s2):
    if s[l] in counter:
        counter[s[l]] += 1
    l+=1

 if max(counter.values) == 0:
    return True
 

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        l = 0
        r = 0
        for c in s1:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        
        while r < len(s2):
            if s2[r] in counter:
                counter[s2[r]] -= 1

            while(r - l + 1) > len(s1) or counter.get(s2[r], 0) < 0:
                if s2[l] in counter:
                    counter[s2[l]] += 1
                l+=1
            print(counter)
            if max(counter.values()) == 0:
                return True

            r += 1
            
        return False
 
        