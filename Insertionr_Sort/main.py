# Insertion Sort

import random as rnd

def init_arr () :
    return [rnd.randint(1, 20) for _ in range(20)]

def insertion_sort (arr) :
    for i in range(len(arr) - 1) :
        p_min = j = i + 1
        min = arr[j]
        while j < len(arr) :
            if min > arr[j] :
                min = arr[j]
                p_min = j
            j += 1
        if min < arr[i] :
            t = arr[i]
            arr[i] = arr[p_min]
            arr[p_min] = t
            
if __name__ == "__main__" :
    arr = init_arr()
    print(arr)
    insertion_sort(arr)
    print(arr)