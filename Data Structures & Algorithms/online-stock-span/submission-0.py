class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        self.data.append(price)
        span = 0

        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] > price:
                break
            
            span += 1

        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)