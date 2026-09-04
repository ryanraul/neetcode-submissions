"""
"OUZODYXAZV"
      l
         r
"XYZ"

- create a counter dictionary to save all the valid values and their frequency
- each iteration
    - decrease the count of the valid characters

- always keep the left pointer in the equivalent char
- only move the left pointer when the current left pointer check count become negative (it means we have more than we need)

- check if the maximum frequency is zero
- if yes:
    - save the current minimum substring

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        result = ""
        counter = {}

        for c in t:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        
        while r < len(s):

            if s[r] in counter:
                counter[s[r]] -= 1

            while l < len(s) and (s[l] not in counter or counter.get(s[l], 0) < 0):
                if s[l] in counter:
                    counter[s[l]] += 1
                l+=1

            if max(counter.values()) == 0:
                size = r - l + 1
                if(len(result) == 0 or size < len(result)):
                    result = "".join(s[l:r+1])

            if l > r:
                r = l
            else:
                r += 1
        
        return result

    