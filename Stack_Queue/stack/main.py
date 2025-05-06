class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("Pop da uno stack vuoto")
        return self.items.pop()

    def peek(self):
        if self.empty():
            raise IndexError("Peek da uno stack vuoto")
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    print(stack.empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.empty())
    print(stack.pop())
    print(stack.empty())