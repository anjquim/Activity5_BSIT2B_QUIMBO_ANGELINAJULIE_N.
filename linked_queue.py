class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow: Cannot dequeue from an empty queue.")

        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return item

    def peek_front(self):
        if self.is_empty():
            raise Exception("Queue Underflow: Queue is empty.")

        return self.front.data

    def __str__(self):
        current = self.front
        result = []

        while current:
            result.append(current.data)
            current = current.next

        return str(result)