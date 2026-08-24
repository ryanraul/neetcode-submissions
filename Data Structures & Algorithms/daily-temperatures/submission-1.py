"""
[30,0]

res = len(temperatures) * [0]
for i, t in enumerate(temperatures)

while stack and stack[-1][0] > t:
    topTemp, topIndex = stack.pop()
    res[topIndex] = i - topIndex

stack.append(t)

return res

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                res[topIndex] = i - topIndex

            stack.append([t,i])

        return res