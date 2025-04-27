import random


def init_arr_stub() :
    arr = [7,1,1,2,2,2,2,3]
    return arr

def init_rnd() :
    arr = [random.choice(10) for _ in range(10)]
    return arr
    
def occurrence_count (arr, k) :
    if len(arr) <= 1 :
        return 1 if arr and arr[0] == k else 0
    
    mid_arr = int(len(arr) // 2)
    left_arr = occurrence_count(arr[:mid_arr], k)
    right_arr = occurrence_count(arr[mid_arr:], k)
    
    return left_arr + right_arr
    
def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid_arr = int(len(arr) // 2)
    left_arr = merge_sort(arr[:mid_arr])
    right_arr = merge_sort(arr[mid_arr:])
    
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr) :
    result = []
    i = j = 0
    
    while i < len(left_arr) and j < len(right_arr) :
        if left_arr[i] < right_arr [j] :
            result.append(left_arr[i])
            i += 1
        else :
            result.append(right_arr[j])
            j += 1 
        
    while i < len(left_arr) :
        result.append(left_arr[i])
        i += 1
        
    while j < len(right_arr) :
        result.append(right_arr[j])
        j += 1
        
    return result

        
if __name__ == "__main__" :
    arr = []
    
    x = int(input("<--- 1 - init_stub --->\n<--- 2 - init_rTest --->\n> "))
    
    if x == 1 :
        arr = init_arr_stub()
    elif x == 2 :
        arr = init_rnd()
        
    arr = merge_sort(arr)
        
    k = int(input("k > "))
        
    print("> ", occurrence_count(arr, k))
    
    