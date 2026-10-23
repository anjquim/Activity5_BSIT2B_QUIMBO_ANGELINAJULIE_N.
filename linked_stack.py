class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Cannot pop from an empty stack.")

        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Stack is empty.")
        return self.top.data

    def __str__(self):
        current = self.top
        result = []

        while current:
            result.append(current.data)
            current = current.next

        return str(result)
