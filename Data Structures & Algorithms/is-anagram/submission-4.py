"""
word1 = aabc
word2 = baac


hash1: {
    a: 2,
    b: 1
    c: 1
}

hash2: {
    a: 2,
    b: 1
    c: 1
}


sort both of the words
and comparte each character



"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): 
            return False

        s_sort = sorted(s)
        t_sort = sorted(t)

        for i in range(len(s)):
            if(s_sort[i] != t_sort[i]):
                return False

        return True