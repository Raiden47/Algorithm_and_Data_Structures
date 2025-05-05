# Heap Sort

import random as rnd

def init_arr():
    return [rnd.randint(1, 20) for _ in range(20)]

# Max_Heap -> A[PARENT(i)] >= A[i]
class MaxHeap:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < self.heap_size and self.arr[l] > self.arr[largest]:
            largest = l
        if r < self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

def build_max_heap(arr):
    heap = MaxHeap(arr)
    for i in range(len(arr) // 2 - 1, -1, -1):
        heap.max_heapify(i)
    return heap

def heapsort(arr):
    heap = build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Scambia il massimo con l'ultimo elemento
        heap.heap_size -= 1  # Riduci la dimensione dell'heap
        heap.max_heapify(0)  # Ripristina la proprietà di max-heap

if __name__ == "__main__":
    arr = init_arr()
    print("Array iniziale:", arr)
    heapsort(arr)
    print("Array ordinato:", arr)