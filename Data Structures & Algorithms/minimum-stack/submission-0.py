class MinStack:
    
    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)
        min_current = min(val, self.min_values[-1] if self.min_values else val)
        self.min_values.append(min_current)

    def pop(self) -> None:
        self.values.pop(-1)        
        self.min_values.pop(-1)        

    def top(self) -> int:
        return self.values[-1]        

    def getMin(self) -> int:
        return self.min_values[-1]        
