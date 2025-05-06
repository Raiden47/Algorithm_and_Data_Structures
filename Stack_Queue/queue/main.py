class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.empty():
            raise IndexError("Dequeue da una coda vuota")
        return self.items.pop(0)

    def peek(self):
        if self.empty():
            raise IndexError("Peek da una coda vuota")
        return self.items[0]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue = Queue()
    print(queue.empty())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.empty())
    print(queue.dequeue())
    print(queue.empty())