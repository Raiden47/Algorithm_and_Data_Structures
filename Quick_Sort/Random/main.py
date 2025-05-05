# Random-Quicksort

import random as rnd

def init_arr () :
    return [rnd.randint(1, 20) for _ in range(20)]

def random_partition (arr, p, r):
    i = rnd.randint(p, r)
    arr[r] , arr[i] = arr[i], arr[r]
    return partition(arr, p, r)

def quicksort(arr, p, r) :
    if p < r :
        q = random_partition (arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
    
# p punta alla prima posizione dell'array
# r punta all'ultima posizione dell'array
def partition (arr, p, r) :
    x = arr[r]
    i = p - 1
    for j in range(p, r) :
        if arr[j] <= x :
            i += 1
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1
        
        

if __name__ == "__main__" :
    arr = init_arr()
    print(arr)
    quicksort(arr, 0, len(arr) -1)
    print(arr)