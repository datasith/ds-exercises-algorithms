def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for b in bombs:
        i, j = b
        field[i][j] = -1
        for row in range(i-1,i+2):
            for col in range(j-1, j+2):
                if 0 <= row < num_rows and 0 <= col < num_cols and field[row][col]!=-1:
                    field[row][col] += 1

    return field

def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

if __name__ == '__main__':
    ans = mine_sweeper([[0, 2], [2, 0]], 3, 3)
    result = [[0, 1, -1],
              [1, 2, 1],
              [-1, 1, 0]]
    assert ans == result, "check yo code"

    ans = mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)
    result = [[-1, -1, 2, 1],
              [2, 3, -1, 1],
              [0, 1, 1, 1]]
    assert ans == result, "check yo code"

    ans = mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)
    result = [[1, 2, 2, 1, 0],
              [1, -1, -1, 2, 0],
              [1, 3, -1, 2, 0],
              [0, 1, 2, 2, 1],
              [0, 0, 1, -1, 1]]
    assert ans == result, "check yo code"
    print( to_string(ans) )
