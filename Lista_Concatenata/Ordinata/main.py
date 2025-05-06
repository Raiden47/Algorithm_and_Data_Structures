class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    sll = SortedLinkedList()
    sll.insert(30)
    sll.insert(10)
    sll.insert(20)
    sll.display()