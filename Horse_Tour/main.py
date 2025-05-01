# Horse tour
# Search for an horse route in order to cross all the cell once

directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

def is_valid (visited, dim, row, col) :
    return (row, col) not in visited and 0 <= row < dim and 0 <= col < dim

def backtrack (res, path, visited, dim, row, col) :
    # Termine ricorsione
    if len(path) >= dim*dim :
        res.append(path[:])
        return
#    for row in range(dim) :
#        for col in range (dim) :
    for dx, dy in directions :
        sx, sy = row + dx, col + dy
        if is_valid(path, dim, sx, sy) :
            path.append((sx, sy))
            visited.add((sx, sy))
            backtrack(res, path, visited, dim, sx, sy)
            visited.remove((sx, sy))
            path.pop()
        
def horse_tour(dim) :
    result = []
    path = []
    visited = set()
    backtrack(result, path, visited, dim, 0, 0)
    return result


if __name__ == '__main__' :
    x = int(input(">> Insert board dimendion > "))
    result = horse_tour(x)
    print(result)
    