class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s1_counter = {}

        for c1 in s1:
            if c1 not in s1_counter:
                s1_counter[c1] = 0
            s1_counter[c1] += 1

        for r in range(len(s2)):
            if s2[r] in s1_counter:
                s1_counter[s2[r]] -= 1
            
            while (r - l + 1) > len(s1) or s1_counter.get(s2[r], 0) < 0:
                if s2[l] in s1_counter:
                    s1_counter[s2[l]] += 1
                l+=1

            if max(s1_counter.values()) == 0:
                return True

        return False


