import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost > dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, w in graph[node]:
                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_cost = cost + w

                    if new_cost < dist[nei][new_count]:
                        dist[nei][new_count] = new_cost
                        heapq.heappush(pq, (new_cost, nei, new_count))

        return -1