"""
5#Hello5#World
       l
       r
size_text = 5
l = r + 1
r = l + size_text
"""
class Solution:
    separator = "#"
    def encode(self, strs: List[str]) -> str:
        response = []
        for text in strs:
            response.append(str(len(text)))
            response.append(self.separator)
            response.append(text)
        
        print("".join(response))
        return "".join(response)

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        response = []
        while l < len(s):
            #r = l
            while s[r] != self.separator:
                r += 1

            size_text = int(s[l:r])
            l = r + 1
            r = l + size_text
            response.append("".join(s[l:r]))
            l = r
        return response
