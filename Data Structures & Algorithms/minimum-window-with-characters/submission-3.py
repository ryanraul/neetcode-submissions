"""
{
 X: 0,
 Y: 0,
 Z: -6,
 V: 0
}

OUZODYXAZZZZZZZV
     l         r
XYZV

{
 X: 0,
 Y: 0,
 Z: -3,
 V: 0
}

OUZODYXAZZZXZZZZVY
           l     r
XYZV

{
    A: 0
    B: 0
    C: 0
}

ADOBECODEBANC
         l  r
ABC
- if our left is negative, move it foward 
- until we find counter valid value again, that is not negative
- 

l = 0
r = 0
res_size = len(s) + 1

for ct in t:
    counter[ct] = 1 + counter.get(ct,0)

for r in range(s):
    if s[r] in counter:
        counter[s[r]] -= 1
    
    while (counter.get(s[l], 0) < 0 or s[l] not in counter) and l < r:
        if s[l] in counter:
            counter[s[l]] += 1
        l+=1
    
    if max(counter.values()) == 0 and (r - l) < res_size:
        res_start = l
        res_star = r
    
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        res_size = len(s) + 1
        res_start = 0
        res_end = 0
        counter = { }

        for ct in t:
            counter[ct] = 1 + counter.get(ct,0)

        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1
            
            while (counter.get(s[l], 0) < 0 or s[l] not in counter) and l < r:
                if s[l] in counter:
                    counter[s[l]] += 1
                l+=1
            
            if max(counter.values()) == 0 and (r - l) < res_size:
                res_start = l
                res_end = r + 1
                res_size = r - l
        
        if res_size == len(s) + 1:
            res_start = 0
            res_end = 0
            res_size = 0

        return s[res_start:res_end]