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
        
        data = self.data[key]
        l = 0
        r = len(data) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            curr = data[mid][0]

            if curr == timestamp: return data[mid][1]

            if curr > timestamp:
                r = mid - 1
            else:
                res = data[mid][1]
                l = mid + 1

        return res