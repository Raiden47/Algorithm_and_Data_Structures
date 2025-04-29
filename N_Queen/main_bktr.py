# Questa funzione controlla che la colonna non sia occupata e l'indice delle diagonali non siano già occupati
def is_valid (row, col, col_occ, p_diag, s_diag) :
    return col not in col_occ and (row - col) not in p_diag and (row + col) not in s_diag


def backtrack (row, dim, result, path, col_occ, p_diag, s_diag) :
    if row == dim :
        result.append(path[:])
        return
    for col in range(dim) :
        if is_valid(row, col, col_occ, p_diag, s_diag) :
            col_occ.add(col)
            p_diag.add(row - col)
            s_diag.add(row + col)
            path.append(col)
            backtrack(row + 1, dim, result, path, col_occ, p_diag, s_diag)
            path.pop()
            col_occ.remove(col)
            p_diag.remove(row - col)
            s_diag.remove(row + col)
            

def n_queen (dim):
    result = []
    path = []
    col_occ = set()
    p_diag = set()
    s_diag = set()
    backtrack(0, dim, result, path, col_occ, p_diag, s_diag)
    return result



def print_result(result):
    for idx, sol in enumerate(result):
        print(f"\nSolution {idx + 1}:")
        for row in sol:
            line = ["-"] * len(sol)
            line[row] = "Q"
            print(" ".join(line))
    

if __name__ == "__main__" :
    n = int(input(">> insert board dimension : "))
    result = n_queen(n)
    
    print(result)
    
    print_result(result)