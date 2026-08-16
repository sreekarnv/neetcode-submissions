class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        span = 1

        while self.data and self.data[-1][0] <= price:
            val = self.data.pop()[1]
            span += val
        
        self.data.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)