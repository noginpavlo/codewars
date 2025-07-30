class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __str__(self):
        return f"Value: {self.value}"


count = Counter(10)
count += 10

print(count)
