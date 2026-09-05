"""
[1,2]
b = 2
a = 1
res = 2+1 = 3
append the response/result
[3,3]
b = 3
a = 3
res = 3 * 3 = 9
[9,4]
b = 4
a = 9
res = a - b = 9 - 4 = 5
[5]
return stack.pop()
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for v in tokens:
            print(v)
            if self.isOperation(v):
                b = int(stack.pop())
                a = int(stack.pop())
                
                if v == "+":
                    res = a + b
                elif v == "-":
                    res = a - b
                elif v == "*":
                    res = a * b
                elif v == "/":
                    res = a / b
                
                stack.append(int(res))
            else:
                stack.append(int(v))
        
        return stack.pop()

    def isOperation(self, value):
        return value == "+" or value == "-" or value == "*" or value == "/"