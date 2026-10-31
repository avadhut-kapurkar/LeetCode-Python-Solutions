class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Memoization for mirror jumps
        # jump_R[(r, c)] stores the final (r_dest, c_dest) when entering mirror (r, c) from the LEFT (moving RIGHT)
        # jump_D[(r, c)] stores the final (r_dest, c_dest) when entering mirror (r, c) from ABOVE (moving DOWN)
        jump_R = {}
        jump_D = {}
        
        def resolve_right(r: int, c: int):
            if (r, c) in jump_R:
                return jump_R[(r, c)]
            
            # Moving right into mirror (r, c) reflects DOWN to (r + 1, c)
            nr, nc = r + 1, c
            if nr >= m or nc >= n:
                res = None
            elif grid[nr][nc] == 0:
                res = (nr, nc)
            else:
                # Hits another mirror coming from above (moving DOWN)
                res = resolve_down(nr, nc)
            
            jump_R[(r, c)] = res
            return res

        def resolve_down(r: int, c: int):
            if (r, c) in jump_D:
                return jump_D[(r, c)]
            
            # Moving down into mirror (r, c) reflects RIGHT to (r, c + 1)
            nr, nc = r, c + 1
            if nr >= m or nc >= n:
                res = None
            elif grid[nr][nc] == 0:
                res = (nr, nc)
            else:
                # Hits another mirror coming from left (moving RIGHT)
                res = resolve_right(nr, nc)
            
            jump_D[(r, c)] = res
            return res

        # dp[r][c] stores number of valid paths from (r, c) to (m - 1, n - 1)
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1  # Base case: destination

        # Fill DP table backwards
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1 or (r == m - 1 and c == n - 1):
                    continue
                
                paths = 0
                
                # Option 1: Try to move RIGHT
                if c + 1 < n:
                    if grid[r][c + 1] == 0:
                        paths = (paths + dp[r][c + 1]) % MOD
                    else:
                        dest = resolve_right(r, c + 1)
                        if dest:
                            paths = (paths + dp[dest[0]][dest[1]]) % MOD
                
                # Option 2: Try to move DOWN
                if r + 1 < m:
                    if grid[r + 1][c] == 0:
                        paths = (paths + dp[r + 1][c]) % MOD
                    else:
                        dest = resolve_down(r + 1, c)
                        if dest:
                            paths = (paths + dp[dest[0]][dest[1]]) % MOD
                
                dp[r][c] = paths

        return dp[0][0]