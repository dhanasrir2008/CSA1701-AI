from collections import deque

def water_jug(x, y, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print((a, b))

        if a == target or b == target:
            return True

        queue.append((x, b))
        queue.append((a, y))
        queue.append((0, b))
        queue.append((a, 0))

        d = min(a, y - b)
        queue.append((a - d, b + d))

        d = min(b, x - a)
        queue.append((a + d, b - d))

    return False

water_jug(4, 3, 2)
