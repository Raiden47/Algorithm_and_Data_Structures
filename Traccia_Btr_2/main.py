import numpy as np

def search_sequence(mat, row, col, string, index, result=None):
    if result is None:
        result = []

    r, c = mat.shape

    if index == len(string):
        return result

    if row >= r:
        return '<--- ERROR --->'

    if col >= c:
        return search_sequence(mat, row + 1, 0, string, index, result)

    if mat[row][col] == string[index]:
        result.append((row, col))
        index += 1
        new_row, new_col, new_index = next_step(mat, row, col, string, index)

        # Se non si è trovato il passo successivo, backtrack
        if (new_row, new_col) == (row, col):
            result.pop()
            index -= 1
            return search_sequence(mat, row, col + 1, string, index, result)
        
        return search_sequence(mat, new_row, new_col, string, new_index, result)

    return search_sequence(mat, row, col + 1, string, index, result)

def next_step(mat, row, col, string, index):
    r, c = mat.shape
    if index >= len(string):
        return row, col, index

    for i in range(max(0, row - 1), min(r, row + 2)):
        for j in range(max(0, col - 1), min(c, col + 2)):
            if (i, j) != (row, col) and mat[i][j] == string[index]:
                return i, j, index + 1

    # Nessuna lettera trovata nelle vicinanze
    return row, col, index - 1

if __name__ == '__main__':
    mat = np.array([
        ['s','r','z','h','d'],
        ['f','o','a','g','e'],
        ['x','d','n','l','o'],
        ['o','r','a','t','n'],
        ['z','p','o','l','n']
    ])

    str_chk = 'helo'
    print(mat)
    result = search_sequence(mat, 0, 0, str_chk, 0, result=None)
    print("\nRisultato:")
    print(result)
