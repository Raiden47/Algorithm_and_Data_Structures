def knapsack_modified(mat, m):
    # Inizializza un set per memorizzare le somme possibili
    possible_sums = {0}

    # Itera su ogni riga della matrice
    for row in mat:
        new_sums = set()
        for value in row:
            for current_sum in possible_sums:
                if current_sum + value <= m:
                    new_sums.add(current_sum + value)
        possible_sums = new_sums

    # Restituisci la somma massima che non supera m
    return max(possible_sums) if possible_sums else None

if __name__ == '__main__':
    m = 20
    a = [[8, 6, 4], [5, 10], [1, 3, 3, 7], [50, 14, 23, 8]]
    b = [[4,6,8],[5,10],[1,3,5,5]]
    c = [[6,4,8],[10,6],[7,3,1,7]]
    solution = knapsack_modified(b, m)
    print("Matrice:", c)
    if solution is not None :
        print("Somma massima minore o uguale a", m, ":", solution)
    else :
        print("no solution")