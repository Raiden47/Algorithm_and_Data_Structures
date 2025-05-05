# Heap Sort

import random as rnd

def init_arr () :
    return [rnd.randint(1, 20) for _ in range(20)]

# Max_Heap -> A[PARENT(i)] >= A[i]
class max_heap :
    
    lenght = 0
    heap_size = 0
    
    def __init__(self, arr) :
        self.lenght = len(arr)
        self.heap_size = self.lenght

    def parent (i) :
        return i // 2

    def left (i) :
        return 2 * i 

    def right (i) :
        return (2 * i) + 1

    def max_heapify(self, arr, i) :
        max = 0
        l = self.left(i)
        r = self.right(i)
        max = l if l <= self.heap_size and arr[l] > arr[i] else i
        # if l <= self.heap_size and arr[l] > arr[i] :
        if r < self.heap_size and arr[r] > arr[max] :
            max = r
        if max != i :
            t = arr[i]
            arr[i] = arr[max]
            arr[max] = t
            self.max_heapify(self, arr, max)
            
def build_max_heap (arr) :
    heap = max_heap()
    heap.__init__(arr)
    for i in range(heap.lenght//2) :
        heap.max_heapify(arr, (heap.lenght//2) - i)
            
def heapsort(arr) :
    heap = max_heap()
    build_max_heap(arr)
    for i in range(len(arr)) :
        if i < 1 :
            arr[0] , a[len(arr) - 1] = a[len(arr) - 1], arr[0]
            heap.heap_size -= 1
            heap.max_heapify(arr, 0)
            
        
    

if __name__ == "__main__" :
    arr = init_arr()
    print(arr)
    heapsort(arr)
    print(arr)