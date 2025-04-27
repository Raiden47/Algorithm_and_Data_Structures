import random

def init() :
    for arr in range (10) :
        arr.append(random.randint(1,100))
    return arr

def init_stub_1() :
    arr = [40, 40]
    return arr
    
def init_stub_2() :
    arr = [10, 2, 6, 8, 4]
    return arr

        
def sort_search(arr, mode, s) :
    
    if mode == 0 :
        if len(arr) <= 1 :
            print("return arr value -> ", arr)
            return arr
    
        mid_arr = int(len(arr) // 2)
        print("mid_arr = ", mid_arr)
    
        l_arr = arr[:mid_arr]
        r_arr = arr[mid_arr:]
        print("arr = ", arr, " left_arr[:mid_arr] = ", l_arr, " right_arr[mid_arr:] = ", r_arr)
    
        left_arr = sort_search(l_arr, mode, s)
        right_arr = sort_search(r_arr, mode, s)
        
        return merge(left_arr, right_arr)
    
    if mode == 1 :
        mid_arr = find_mid_value(arr, 0, s)
        left_arr = arr[:mid_arr]
        right_arr = arr[mid_arr:]
        print("left_arr -> ", left_arr, "\nmid_arr -> ", mid_arr, "\nright_arr -> ", right_arr)
        return num_search (left_arr, right_arr, s)
    
def find_mid_value(arr, index, s) :
    mid_val = int(s // 2)
    print("index -> ", index)
    if arr[index] < mid_val :
        return find_mid_value(arr, index + 1, s)
    elif index == 0:
        return index + 1
    else :
        return index

def merge(left_arr, right_arr) :
    result = []
    i = j = 0 
    
    while i < len(left_arr) and j < len(right_arr) :
        if left_arr[i] < right_arr[j] :
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
    
def num_search (left_arr, right_arr, s) :
    result = [0, 0, s]
    i = 0
    j = len(right_arr) - 1
    
    while i < len(left_arr) and j >= 0 :
        print( str(left_arr[i]) , " + " , str(right_arr[j]) , " = " , str(left_arr[i] + right_arr[j]), " abs(", abs(left_arr[i] - right_arr[j]) ,")")
        
        total = left_arr[i] + right_arr[j]
        diff = abs(left_arr[i] - right_arr[j])
        
        if total == s and diff < result[2] :
            result = [left_arr[i], right_arr[j], diff]
            
        if total < s :
            i += 1
        else :
            j -= 1
    
    return result

    
if __name__ == "__main__" :
    
    arr = []
    
    x = int(input("<--- 1 - Test1 --->\n<--- 2 - Test2 --->\n<--- 3 - TestR --->\n> "))
    print("vector init...\n")
    
    if x == 1 :
        arr = init_stub_1()
    elif x == 2 :
        arr = init_stub_2()
    elif x == 3 :
        arr = init()
        
    arr = sort_search(arr, 0, 0)
        
    s = int(input("input s value > "))
    print("search for sub-set")
    res = sort_search(arr, 1, s)
    
    if res[0] != 0 and res[1] != 0 :
        print("Xi = " + str(res[0]) + " Yi = " + str(res[1]) + " d = " + str(res[2]))
    else :
        print("Xi = " + str(res[0]) + " Yi = " + str(res[1]) + " d = " + str(res[2]))
        print("<-- Error -->")
    