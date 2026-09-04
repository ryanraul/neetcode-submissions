"""

main values of the stack [1,2]
history of min values :  [1,1]

"""

class MinStack:
    
    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        current_min = min(val, self.min_values[-1] if self.min_values else val)
        self.min_values.append(current_min)
        self.values.append(val)

    def pop(self) -> None:
        self.min_values.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
