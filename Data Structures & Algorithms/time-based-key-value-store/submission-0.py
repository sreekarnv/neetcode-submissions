class TimeMap:

    def __init__(self):
        self.data = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        values = self.data[key]

        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            mid_timestamp = values[mid][0]

            if mid_timestamp <= timestamp:
                result = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return result