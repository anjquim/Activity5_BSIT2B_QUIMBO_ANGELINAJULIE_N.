class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue Overflow: Cannot enqueue into a full queue.")

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow: Cannot dequeue from an empty queue.")

        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise Exception("Queue Underflow: Queue is empty.")
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "[]"

        result = []
        index = self.front

        for _ in range(self.size):
            result.append(self.queue[index])
            index = (index + 1) % self.capacity

        return str(result)


# Wrap around demonstration

q = ArrayQueue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.dequeue()
q.dequeue()

q.enqueue(5)
q.enqueue(6)

print(q)