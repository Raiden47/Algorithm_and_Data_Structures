import numpy as np

# Direzioni: alto-sx, alto, alto-dx, sx, dx, basso-sx, basso, basso-dx
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def is_valid(r, c, rows, cols, visited):
    return 0 <= r < rows and 0 <= c < cols and not visited[r][c]

def dfs(mat, word, index, row, col, visited, path):
    if index == len(word):
        return True

    rows, cols = mat.shape

    if not is_valid(row, col, rows, cols, visited):
        return False

    if mat[row][col] != word[index]:
        return False

    visited[row][col] = True
    path.append((row, col))

    for dr, dc in DIRECTIONS:
        if dfs(mat, word, index + 1, row + dr, col + dc, visited, path):
            return True

    # Backtrack
    visited[row][col] = False
    path.pop()

    return False

def find_word_in_matrix(mat, word):
    rows, cols = mat.shape
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == word[0]:
                path = []
                if dfs(mat, word, 0, r, c, visited, path):
                    return path

    return None  # parola non trovata

if __name__ == '__main__':
    mat = np.array([
        ['s','r','z','h','d'],
        ['f','o','a','g','e'],
        ['x','d','n','l','o'],
        ['o','r','a','t','n'],
        ['z','p','o','l','n']
    ])
    
    word = 'helo'

    print("Matrice:")
    print(mat)

    result = find_word_in_matrix(mat, word)

    if result:
        print(f"\nParola '{word}' trovata! Percorso: {result}")
    else:
        print(f"\nParola '{word}' NON trovata nella matrice.")
