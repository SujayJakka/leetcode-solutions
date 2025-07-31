class TimeMap:

    def __init__(self):
        self.h_map_value = {}
        self.time_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h_map_value[(key, timestamp)] = value

        if key not in self.time_map:
            self.time_map[key] = [timestamp]
        else:
            self.time_map[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.time_map or self.time_map[key][0] > timestamp:
            return ""
        
        arr = self.time_map[key]
        l , r = 0, len(arr) - 1

        prev_time = -1

        while l <= r:
            mid_index = (l + r) // 2
            mid_value = arr[mid_index]

            if mid_value == timestamp:
                return self.h_map_value[(key, mid_value)]

            elif mid_value < timestamp:
                l = mid_index + 1
                prev_time = mid_value
            else:
                r = mid_index - 1
            
        return self.h_map_value[(key, prev_time)]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)