# number of possible sets of closing branches

class Solution:
    def numberOfSets(self, n, maxDistance, roads):
        INF = float('inf')
        ans = 0

        # Try all subsets (nodes to KEEP)
        for mask in range(1 << n):
            active = [i for i in range(n) if mask & (1 << i)]

            # 0 or 1 node → always valid
            if len(active) <= 1:
                ans += 1
                continue

            # Build distance matrix ONLY for active nodes
            dist = [[INF] * n for _ in range(n)]
            for i in active:
                dist[i][i] = 0

            # Add only edges between active nodes
            for u, v, w in roads:
                if (mask & (1 << u)) and (mask & (1 << v)):
                    dist[u][v] = min(dist[u][v], w)
                    dist[v][u] = min(dist[v][u], w)

            # Floyd-Warshall ONLY on active nodes
            for k in active:
                for i in active:
                    for j in active:
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

            # Check distances
            valid = True
            for i in range(len(active)):
                for j in range(i + 1, len(active)):
                    if dist[active[i]][active[j]] > maxDistance:
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                ans += 1

        return ans