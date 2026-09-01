class StockSpanner:

    def __init__(self):
        self.st = []
        self.res = {}

    def next(self, price: int) -> int:
        span = 1
        while len(self.st) > 0 and self.st[-1] <= price:
            span += self.res[self.st[-1]]
            self.st.pop()
        self.res[price] = span
        self.st.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)