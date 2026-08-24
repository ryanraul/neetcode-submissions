"""
setup: 
- create an array with the same size of temperatures
    - with zero in all positions
- create a stack to save [temperature, index]

iterate through temperatures:
    get the index and the temperature value
    while the stack is not empty and current t (temperature) greater than top stack temperature:
        pop the top element of the stack
            get the topTemperature and topIndex
            set at the topIndex position on res array how many days take to find a bigger temperature
                calculus: i (current index) - topIndex
        append the current temperature and index temperature on the stack
    return the res array
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                topT, topI = stack.pop()
                res[topI] = (i - topI)
            stack.append([t, i])

        return res