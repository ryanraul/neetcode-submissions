"""
[
    {
        key: "alice"
        values: [
            {
                time: 1,
                value: "happy"
            },
            {
                time: 3,
                value: "sad"
            },
        ]
    },
    {
        key: "peter"
        values: [
            {
                time: 4,
                value: "happy"
            },
        ]
    }
]

["TimeMap", 
"set", ["test", "one", 10], 
"set", ["test", "two", 20], 
"set", ["test", "three", 30], 
"get", ["test", 15], 
"get", ["test", 25], 
"get", ["test", 35]]

t = 15
[10,20,30]
    lr
    m
"""

class TimeMap:
    def __init__(self):
        self.maps = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = []

        self.maps[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""

        l = 0
        r = len(self.maps[key]) - 1

        mapValue = self.maps[key]

        if timestamp < mapValue[l][0]:
            return ""

        while l <= r:
            m = (l+r)//2

            if timestamp == mapValue[m][0]:
                return mapValue[m][1]

            if timestamp < mapValue[m][0]:
                r = m - 1
            else:
                res = m
                l = m + 1
        
        return mapValue[res][1]
