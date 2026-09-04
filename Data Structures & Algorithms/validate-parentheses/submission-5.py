"""
"([{}])"

""
if the current char is an open brackets 
    keep adding in the stack
otherwise check if the stack has values and pop the stack and check
    if the popped value is compatible with the current bracket
        if yes continue
    otherwise its not a valid input
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack_brackets = []

        for i, c in enumerate(s):
            if self.isOpen(c):
                stack_brackets.append(c)
                continue
            
            if len(stack_brackets) > 0 and self.isCompatibleBracket(c, stack_brackets.pop()):
                continue
            else:
                return False

        return len(stack_brackets) == 0
    
    def isOpen(self, value):
        return value == "(" or value ==  "{" or value == "["

    def isCompatibleBracket(self, close_value, open_value):
        if open_value == "(":
            return close_value == ")"
        elif open_value == "{":
            return close_value == "}"
        elif open_value == "[":
            return close_value == "]"
        else:
            return False
