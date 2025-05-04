# Merge Sort

import random as rnd

def init_arr () :
    return [rnd.randint(1, 20) for _ in range(20)]

def merge_sort (arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = int(len(arr) // 2)
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge (left, right)

def merge (left, right) :
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            res.append(left[i])
            i += 1
        else :
            res.append(right[j])
            j += 1
            
    while i < len(left) :
        res.append(left[i])
        i += 1 
    
    while j < len(right) :
        res.append(right[j])
        j += 1
        
    return res

if __name__ == "__main__" :
    arr = init_arr()
    print(arr)
    arr = merge_sort(arr)
    print(arr)