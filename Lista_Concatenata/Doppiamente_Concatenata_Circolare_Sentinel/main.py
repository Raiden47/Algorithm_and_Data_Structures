class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def append(self, data):
        new_node = Node(data)
        tail = self.sentinel.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.sentinel
        self.sentinel.prev = new_node

    def display(self):
        current = self.sentinel.next
        while current != self.sentinel:
            print(current.data, end=" <-> ")
            current = current.next
        print("(sentinel)")

if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.append(10)
    cdll.append(20)
    cdll.append(30)
    cdll.display()