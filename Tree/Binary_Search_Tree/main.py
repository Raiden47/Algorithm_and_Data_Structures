class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, node):
        if node:
            self.inorder_tree_walk(node.left)
            print(node.key, end=" ")
            self.inorder_tree_walk(node.right)

    def tree_search(self, node, key):
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self.tree_search(node.left, key)
        else:
            return self.tree_search(node.right, key)

    def iterative_tree_search(self, node, key):
        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def tree_minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def tree_maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def tree_successor(self, node):
        if node.right:
            return self.tree_minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def tree_insert(self, key):
        new_node = Node(key)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, key):
        node = self.tree_search(self.root, key)
        if node is None:
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = self.tree_minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.tree_insert(15)
    bst.tree_insert(6)
    bst.tree_insert(18)
    bst.tree_insert(3)
    bst.tree_insert(7)
    bst.tree_insert(17)
    bst.tree_insert(20)
    bst.tree_insert(2)
    bst.tree_insert(4)
    bst.tree_insert(13)
    bst.tree_insert(9)

    print("Inorder tree walk:")
    bst.inorder_tree_walk(bst.root)
    print("\n")

    print("Search for key 13:")
    result = bst.tree_search(bst.root, 13)
    print(result.key if result else "Not found")

    print("Minimum key:", bst.tree_minimum(bst.root).key)
    print("Maximum key:", bst.tree_maximum(bst.root).key)

    print("Successor of 13:")
    node = bst.tree_search(bst.root, 13)
    successor = bst.tree_successor(node)
    print(successor.key if successor else "No successor")

    print("Deleting key 13...")
    bst.tree_delete(13)
    print("Inorder tree walk after deletion:")
    bst.inorder_tree_walk(bst.root)
    print()