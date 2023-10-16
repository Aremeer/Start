class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        if capacity < 0: raise ValueError
        self.capacity = capacity

    def __str__(self):
        return "".join("🍪" for _ in range(self.size))

    def deposit(self, n):
        if self.size + n > self.capacity: raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0: raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size