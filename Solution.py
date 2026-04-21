//  O(1) Memory Mathematical Shortcut
from math import gcd

class Solution:
    def minSteps(self, m, n, d):
        if d > max(m, n):
            return -1
        if d % gcd(m, n) != 0:
            return -1

        def pour(fromCap, toCap, target):
            fromJug, toJug, steps = fromCap, 0, 1
            while fromJug != target and toJug != target:
                temp = min(fromJug, toCap - toJug)
                toJug += temp
                fromJug -= temp
                steps += 1
                if fromJug == target or toJug == target:
                    break
                if fromJug == 0:
                    fromJug = fromCap
                    steps += 1
                if toJug == toCap:
                    toJug = 0
                    steps += 1
            return steps

        return min(pour(m, n, d), pour(n, m, d))
// BFS (Breadth First Search) Solution
 from math import gcd
from collections import deque

class Solution:
    def minSteps(self, m, n, d):
        if d > max(m, n):
            return -1
        if d % gcd(m, n) != 0:
            return -1

        visited = [[False] * (n + 1) for _ in range(m + 1)]
        q = deque([((0, 0), 0)])
        visited[0][0] = True

        while q:
            (x, y), steps = q.popleft()
            if x == d or y == d:
                return steps

            next_states = [
                (m, y),
                (x, n),
                (0, y),
                (x, 0)
            ]

            pour = min(x, n - y)
            next_states.append((x - pour, y + pour))

            pour = min(y, m - x)
            next_states.append((x + pour, y - pour))

            for nx, ny in next_states:
                if 0 <= nx <= m and 0 <= ny <= n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append(((nx, ny), steps + 1))

        return -1
