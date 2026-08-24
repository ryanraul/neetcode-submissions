"""


"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def makeOperation(operator):
            a = stack.pop()
            b = stack.pop()
            match(operator):
                case '+':
                    return a + b
                case '-':
                    return b - a
                case '*':
                    return a * b
                case '/':
                    return int(float(b)/a)
            return 0

        for t in tokens:
            if t in '+-*/':
                stack.append(makeOperation(t))
                continue

            stack.append(int(t))
        
        return stack.pop()
    
        
