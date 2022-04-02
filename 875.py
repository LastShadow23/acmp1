DEAD_CELL = '.'
ALIVE_CELL = '*'

def get_neigh_count(arr, row, col):
    neigh_count = 0
    offset = ((-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1))

    for ofs in offset:
        neigh_count += arr[(row + ofs[0]) % n] \
                          [(col + ofs[1]) % m] == ALIVE_CELL
        if neigh_count > 3:
            break

    return neigh_count

n, m, k = map(int, input().split())
arr = [[char for char in input()] for _ in range(n)]

for _ in range(k):
    arr = [[ALIVE_CELL if arr[row][col] == DEAD_CELL \
            and get_neigh_count(arr, row, col) == 3 \
            or arr[row][col] == ALIVE_CELL \
            and get_neigh_count(arr, row, col) in (2, 3) \
            else DEAD_CELL for col in range(m)] for row in range(n)]

for row in arr:
    print(*row, sep='')

