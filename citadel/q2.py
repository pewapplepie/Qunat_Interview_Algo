def minMoves(n, startRow, startCol, endRow, endCol):
    if startRow == endRow and startCol == endCol:
        return 0
    
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

    visited = [[False] * n for _ in range(n)]
    visited[startRow][startCol] = True

    # Initialize the BFS queue
    queue = [(startRow, startCol, 0)]  # Each element is a tuple (row, col, moves)

    while queue:
        row, col, num_moves = queue.pop(0)

        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy

            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col]:
                visited[new_row][new_col] = True

                if (new_row, new_col) == (endRow, endCol):
                    return num_moves + 1

                queue.append((new_row, new_col, num_moves + 1))

    return -1  # No path found

print(minMoves(9, 4, 4, 4, 8))