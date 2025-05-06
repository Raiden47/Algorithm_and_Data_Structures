# Radix Sort

import random as rnd

def init_arr():
    return [rnd.randint(1, 20) for _ in range(20)]

def counting_sort_by_digit(x_arr, exp):
    n = len(x_arr)
    output = [0] * n  # Array di output
    count = [0] * 10  # Contatore per le cifre (0-9)

    # Conta le occorrenze delle cifre
    for i in range(n):
        index = (x_arr[i] // exp) % 10
        count[index] += 1
        print(f"ind({index}) - count[index] + 1 ({count[index]})\ncount -> {count}\n")

    # Calcola le posizioni cumulative
    for i in range(1, 10):
        count[i] += count[i - 1]
        print(f"count[i] + count[i - 1]({count[i]})\ncount -> {count}\n")

    # Costruisci l'array ordinato
    for i in range(n - 1, -1, -1):
        index = (x_arr[i] // exp) % 10
        output[count[index] - 1] = x_arr[i]
        count[index] -= 1
        print(f"ind({index}) output[count[index] - 1]({output[count[index] - 1]}) - count[index] - 1 ({count[index]}) - x_arr[i]({x_arr[i]})\ncount -> {count}\noutput -> {output}\n")

    return output

def radix_sort(x_arr):
    # Trova il numero massimo per determinare il numero di cifre
    max_value = max(x_arr)

    # Applica il Counting Sort per ogni cifra
    exp = 1  # exp rappresenta 10^0, 10^1, 10^2, ...
    while max_value // exp > 0:
        x_arr = counting_sort_by_digit(x_arr, exp)
        exp *= 10

    return x_arr

if __name__ == "__main__":
    arr = init_arr()
    print("Array originale:", arr)
    sorted_arr = radix_sort(arr)
    print("Array ordinato:", sorted_arr)