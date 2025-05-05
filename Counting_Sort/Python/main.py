# Counting Sort

import random as rnd

def init_arr():
    return [rnd.randint(1, 20) for _ in range(20)]

def counting_sort(x_arr, k):
    z_arr = [0 for _ in range(k + 1)]
    y_arr = [0 for _ in range(len(x_arr))]

    for i in range(len(x_arr)):
        z_arr[x_arr[i]] += 1
    
    for i in range(1, k + 1):
        z_arr[i] += z_arr[i - 1]

    for i in range(len(x_arr) - 1, -1, -1):  
        y_arr[z_arr[x_arr[i]] - 1] = x_arr[i]
        z_arr[x_arr[i]] -= 1

    return y_arr

if __name__ == "__main__":
    arr = init_arr()
    max_value = max(arr)
    print(arr)
    sorted_arr = counting_sort(arr, max_value)
    print(sorted_arr)