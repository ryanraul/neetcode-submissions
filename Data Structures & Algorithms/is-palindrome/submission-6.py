"""
two pointers
Was it a car or a cat I saw?
    l                 r


"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        def isCharacter(value):
            return (ord('A') <= ord(value) <= ord('Z') or
                    ord('a') <= ord(value) <= ord('z') or
                    ord('0') <= ord(value) <= ord('9'))

        while l < r:
            if not isCharacter(s[l]):
                l+=1
                continue
            if not isCharacter(s[r]):
                r-=1
                continue
            
            if(s[l].lower() != s[r].lower()):
                print(s[l].lower())
                print(s[r].lower())
                return False
            
            l+=1
            r-=1

        return True
