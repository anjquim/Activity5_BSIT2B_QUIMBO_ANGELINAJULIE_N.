class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow: Cannot push onto a full stack.")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Cannot pop from an empty stack.")
        item = self.items[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Stack is empty.")
        return self.items[self.top]

    def __str__(self):
        if self.is_empty():
            return "[]"
        return str(self.items[:self.top + 1])