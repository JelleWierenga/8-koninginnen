board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

locations = []


for i in range(8):
    row, col = map(int, input("Enter the row and column of the piece (e.g., 3 4): ").split())
    locations.append((row, col))

for loc in locations:
    board[loc[0]][loc[1]] = 1

for test in range(8):
    item = locations[test]

    if sum(board[item[0]][0:8]) > 1:
        print(f"More than one piece in row {item[0]}")
        print(f"Conflict at: {item}")

    if sum([board[i][item[1]] for i in range(8)]) > 1:
        print(f"More than one piece in column {item[1]}")
        print(f"Conflict at: {item}")

    row, col = item[0], item[1]

    count_major_diag = 0
    for loc in locations:
        if (loc[0] - loc[1]) == (row - col):
            count_major_diag += 1
    if count_major_diag > 1:
        print(f"More than one piece on the major diagonal at {item}")

    count_minor_diag = 0
    for loc in locations:
        if (loc[0] + loc[1]) == (row + col):
            count_minor_diag += 1
    if count_minor_diag > 1:
        print(f"More than one piece on the minor diagonal at {item}")