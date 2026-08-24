
"""
"zxyzxyz"
   l r

 res =  r - l + 1 
        4 - 2 + 1 = 3
counter = {
    z = 1,
    x = 1,
    y = 1
}
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        counter = {}
        res = 0

        for r in range(len(s)):
            if s[r] not in counter:
                counter[s[r]] = 0

            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
