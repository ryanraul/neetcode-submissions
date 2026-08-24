"""
maps = {
    "alice": {
        timevalues: [
            {
                value: "happy",
                time: 1
            },
            {
                value: "sad",
                time: 3
            }
        ]
    },
    "john": {
        timevalues: [
            {
                value: "happy",
                time: 3
            }
        ]
    }
} 

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

        map_values = self.maps[key]

        if timestamp < map_values[l][0]:
            return ""

        while l <= r:
            mid = (l+r)//2

            if map_values[mid][0] == timestamp:
                return map_values[mid][1]

            if map_values[mid][0] > timestamp:
                r = mid - 1
            else:
                res = mid
                l = mid + 1

        return map_values[res][1]
