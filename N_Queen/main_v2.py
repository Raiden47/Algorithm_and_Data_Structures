def n_queen(mat, row, col) :
    result = []
    
    while True :
        row, col = find_pos(mat, row, col)
        if row is None or col is None :
            break
        mat[row][col] = 1
        result.append((row, col))
        mat_adj(mat, row, col)
        
    return result

def n_queen_backtrack(mat, row, col, res) :
    new_res = n_queen(mat, row, col)
    print(res)
    print (new_res)
    if col >= len(mat) :
        return res
    
    if len(res) < len(new_res) :
        return n_queen_backtrack(mat, row, col + 1, new_res)
    
    return n_queen_backtrack(mat, row, col + 1, res)

def find_pos(mat, row, col) :
    if row >= len(mat) : 
        return None, None
    elif col >= len(mat) :
        return find_pos(mat, row + 1, 0)
    elif mat[row][col] == 0 :
        return row, col
    else :
        return find_pos(mat, row, col + 1)
    
def mat_adj(mat, row, col):
    direction = [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)]
    
    for dx, dy in direction :
        nx, ny = row + dx, col + dy
        while 0 <= nx < len(mat) and 0 <= ny < len(mat) :
            mat[nx][ny] = 1 
            nx += dx
            ny += dy
    

if __name__ == '__main__' :
    result = []
    dim = int(input("<--- Insert board dimendion --->\n> "))
    mat = [[0 for _ in range(dim)] for _ in range(dim)]
    result = n_queen_backtrack(mat, 0, 1, result)
    print(f"Numero di queen posizionate: {len(result)}\nPosizioni delle N queen: {result}")
    