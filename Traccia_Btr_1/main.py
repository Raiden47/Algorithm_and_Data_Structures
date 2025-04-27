def init_stub_1() :
    return "XYZ"

def init_stub_2() :
    return "ABCDE"


def arr_spaced(arr) :
    result = []
    
    if not arr :
        return
    
    result = backtrack(arr, arr[0], result, 1)
    
    return result
    

def backtrack(arr, partial, result, index) :
    if index == len(arr) :
        result.append(partial)
        return
    
    backtrack(arr, partial + arr[index], result, index + 1)
    backtrack(arr, partial + " " + arr[index], result, index + 1)
    
    return result
          
    

if __name__ == "__main__" :
    arr = []
    x = int(input("<--- 1 - test 1 --->\n<--- 2 - test 2 --->\n> "))
    
    if x == 1 :
        print("<-- init stub 1 -->")
        arr = init_stub_1()
    elif x == 2 :
        print("<-- init stub 2 -->")
        arr = init_stub_2()
           
    for txt in arr_spaced(arr) :
        print(txt)
        
        
    