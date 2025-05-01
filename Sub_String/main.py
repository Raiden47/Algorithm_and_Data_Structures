###################################################################################################

# Data un vettore che può contenere numeri interi sia positivi che negativi, trovare il sottoarray
# di numeri contigui che ha la somma più grande, e riportare tale somma
# Sample Input

# -1 -3 4 2
# -1 2 -5 7
# END
# Sample Output
# 6
# 7

###################################################################################################

import random

def init_arr_1():
    return (-1, -3, 4, 2)

def init_arr_2():
    return (-1, 2, -5, 7)

def init_arr_rnd(rng, n_elem) :
    arr = [(random.choice(rng) - (rng // 2)) for _ in range(n_elem)]
    return arr

def search_max_sum(arr, sum, res, index) : 
    if index == len(arr) :
        res.append(sum)
        return
    
    sum += arr[index]
    search_max_sum(arr, sum, res, index + 1)
    search_max_sum(arr, 0, res, index + 1)
        
if __name__ == "__main__" :
    arr = init_arr_2()
    res = []
    
    search_max_sum(arr, 0, res, 0)
    print(f"{max(res)}")
     