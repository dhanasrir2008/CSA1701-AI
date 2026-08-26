# Alpha-Beta Pruning

def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        value = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            value = max(value, alphabeta(
                depth - 1, child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in [node * 2, node * 2 + 1]:
            value = min(value, alphabeta(
                depth - 1, child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


result = alphabeta(3, 5, float('-inf'), float('inf'), True)
print("Best value:", result)
