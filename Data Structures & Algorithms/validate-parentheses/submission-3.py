"""
stack = 
"""
class Solution:
    def isValid(self, s: str) -> bool:
        def isOpen(c) -> bool:
            return c == '{' or c == '[' or c == '('

        def getCloseByOpen(c) -> bool:
            match c:
                case '{':
                    return '}'
                case '(':
                    return ')'
                case '[':
                    return ']'

        stack = []
        for c in s:
            if isOpen(c):
                stack.append(c)
                continue
            
            if len(stack) > 0 and getCloseByOpen(stack[-1]) == c:
                stack.pop()
            else:
                return False

        return len(stack) == 0




