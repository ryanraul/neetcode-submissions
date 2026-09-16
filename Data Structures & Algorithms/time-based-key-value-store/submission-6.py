"""

{
    "alice": {
        "timestamp": "value",
        "1": "happy",
    }
}

TimeMap {
    time_keys = {}

    time_keys[keys] = []
    time_keys[keys].append([timestamp, value])

    list_time_values = time_keys[keys]
    
        0        1         2   
    [[1,"a"], [3, "b"], [4,"c"]]
        l        mid        
        r
    if target == list_time_values[mid][0]:
        return list_time_values[mid][1]
    
    if target > list_time_values[mid][0]:
        l = mid + 1
    else:
        r = mid - 1

    res = list_time_values[l][1]


    [[10,"one"], [20, "two"], [3,"three"]]
        l            mid             r

}   

"""
class TimeMap:

    time_keys = {}

    def __init__(self):
        self.time_keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_keys:
            self.time_keys[key] = []
        self.time_keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_keys or key not in self.time_keys or not self.time_keys[key]:
            return ""
        
        l = 0
        r = len(self.time_keys[key]) - 1
        values_time = self.time_keys[key]
        res = ""

        while l <= r:
            mid = (l+r) // 2

            if values_time[mid][0] == timestamp:
                return values_time[mid][1]
            
            if timestamp > values_time[mid][0]:
                res = values_time[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
