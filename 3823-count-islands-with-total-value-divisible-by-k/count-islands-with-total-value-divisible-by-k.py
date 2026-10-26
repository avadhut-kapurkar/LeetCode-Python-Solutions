class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            stack = [(i, j)]
            total = 0
            grid[i][j] = 0

            while stack:
                x, y = stack.pop()
                total += original[x][y]

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                        stack.append((nx, ny))
                        grid[nx][ny] = 0

            return total

        original = [row[:] for row in grid]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)
                    if total % k == 0:
                        ans += 1

        return ans