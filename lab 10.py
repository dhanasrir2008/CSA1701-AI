import heapq

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',1),('E',5)],
    'C':[('F',2)],
    'D':[], 'E':[], 'F':[]
}

h = {'A':6,'B':4,'C':4,'D':0,'E':0,'F':0}

def astar(start, goal):
    pq = [(0, start)]
    cost = {start:0}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            return cost[node]

        for neigh, w in graph[node]:
            new_cost = cost[node] + w
            if neigh not in cost or new_cost < cost[neigh]:
                cost[neigh] = new_cost
                priority = new_cost + h[neigh]
                heapq.heappush(pq, (priority, neigh))

    return None

print(astar('A','D'))
