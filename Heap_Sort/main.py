# Heap Sort

import random as rnd

def init_arr () :
    return [rnd.randint(1, 20) for _ in range(20)]

# Max_Heap -> A[PARENT(i)] >= A[i]
class max_heap :

    def parent (i) :
        return i // 2

    def left (i) :
        return 2 * i 

    def right (i) :
        return (2 * i) + 1

    def max_heapify(arr, i) :
    

if __name__ == "__main__" :
    arr = init_arr()
    print(arr)
    # arr = ___ (arr)
    print(arr)