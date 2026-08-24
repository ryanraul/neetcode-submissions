"""

"eidboaoo"
l    r
{
    a: 1
    b: 0
}

while r < len(s)

if s[r] in counter:
    counter[s[r]] -= 1

while s[r] in counter and counter[s[r]] < 0:
    if s[l] in counter:
        counter[s[l]] += 1
    l += 1

if max(counter.values()) == 0:
    return True


return false

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = 0
        counter = {}
        for c1 in s1:
            if c1 not in counter:
                counter[c1] = 0
            counter[c1] += 1

        while r < len(s2):
            if s2[r] in counter:
                counter[s2[r]] -= 1

            while (r - l + 1) > len(s1) or counter.get(s2[r], 0) < 0: 
                if s2[l] in counter:
                    counter[s2[l]] += 1
                l += 1

            if max(counter.values()) == 0:
                return True

            r+=1

        return False
        