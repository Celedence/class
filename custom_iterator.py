class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return iter("hello")

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num



c = Counter(0,10)
iter(c)

for x in Counter(0,10):
    print(x)