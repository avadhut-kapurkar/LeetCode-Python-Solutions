
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            p = items[i][1]
            bonus = free[i]
            old = dp[:]

            for r in range(min(p, budget + 1)):
                best = float('-inf')

                for t in range((budget - r) // p + 1):
                    b = r + t * p

                    if t > 0:
                        best = max(best, old[b - p] - (t - 1))

                    if best != float('-inf'):
                        dp[b] = max(dp[b], t + bonus + best)

        return dp[budget]
