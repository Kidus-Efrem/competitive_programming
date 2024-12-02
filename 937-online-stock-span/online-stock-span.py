class StockSpanner(object):
    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price):
        self.day += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:
            span = self.day
        else:
            span = self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        return span
        


