"""Ch04"""

def cover(board, label=1, top=0, left=0, side=None):
    """cover board with a missing corner"""

    if side is None:
        side = len(board)

    # side of sub-board
    sub_side = side // 2

    offsets = (0, -1), (side - 1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top + dy_outer][left + dx_outer]:
                # label the inner corner
                board[top + sub_side + dy_inner][left + sub_side + dx_inner] = label

    print_board(board)
    # next label
    label += 1
    # recursively do the label for its subboard
    if sub_side > 1:
        for dy in [0, sub_side]:
            for dx in [0, sub_side]:
                label = cover(board, label, top + dy, left + dx, sub_side)

    return label

def print_board(board):
    for row in board:
        print((" %2i" * 8) % tuple(row))
    print("#" * 16)
