# Minimax Algorithm for Gaming

def minimax(depth, node, maximizing):
    if depth == 0:
        return node

    if maximizing:
        return max(
            minimax(depth - 1, node * 2, False),
            minimax(depth - 1, node * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth - 1, node * 2, True),
            minimax(depth - 1, node * 2 + 1, True)
        )

print("Best value:", minimax(3, 5, True))
