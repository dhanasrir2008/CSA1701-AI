from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def bfs():
    start = (3,3,1)
    goal = (0,0,0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m,c,b), path = queue.popleft()

        if (m,c,b) == goal:
            return path + [(m,c,b)]

        visited.add((m,c,b))

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for x,y in moves:
            if b == 1:
                new = (m-x, c-y, 0)
            else:
                new = (m+x, c+y, 1)

            if 0<=new[0]<=3 and 0<=new[1]<=3 and is_valid(new[0], new[1]):
                if new not in visited:
                    queue.append((new, path+[(m,c,b)]))
    return None

print(bfs())
