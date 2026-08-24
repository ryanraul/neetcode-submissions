"""

"zxyzxyz"
     l
       r
{
    z: 2
    x: 0
    y: 1
}
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        r = 0
        res = 1
        counter = {}

        while r < len(s):
            if s[r] not in counter:
                counter[s[r]] = 0
            
            counter[s[r]]+=1
            while counter[s[r]] == 2:
                counter[s[l]] -= 1
                l+=1
            
            res = max(res, r - l + 1)
            r+=1
        
        return res




        