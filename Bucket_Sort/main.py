import random as rnd

def init_array(size):
    return [round(rnd.uniform(0, 1), 2) for _ in range(size)]

def bucket_sort(arr):
    # Creazione dei bucket
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribuzione degli elementi nei bucket
    for num in arr:
        index = int(num * n)  # Calcola l'indice del bucket
        buckets[index].append(num)

    # Ordinamento dei bucket
    for bucket in buckets:
        bucket.sort()

    # Concatenazione dei bucket
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

if __name__ == "__main__":
    arr = init_array(10)
    print("Array originale:", arr)
    sorted_arr = bucket_sort(arr)
    print("Array ordinato:", sorted_arr)