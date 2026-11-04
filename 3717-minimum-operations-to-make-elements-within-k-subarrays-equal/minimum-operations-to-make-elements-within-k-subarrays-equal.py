import heapq
from collections import defaultdict

class SlidingWindowMedian:
    def __init__(self, k):
        self.k = k
        self.low = []   # Max-heap (stores negative numbers)
        self.high = []  # Min-heap
        self.delayed = defaultdict(int)
        
        self.low_size = 0
        self.high_size = 0
        self.low_sum = 0
        self.high_sum = 0

    def prune(self, heap, is_low):
        """Removes elements from the top of the heap that have been marked for deletion."""
        while heap:
            num = -heap[0] if is_low else heap[0]
            if self.delayed[num] > 0:
                self.delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def rebalance(self):
        """Maintains size property: low_size == high_size or low_size == high_size + 1."""
        if self.low_size > self.high_size + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
            self.low_sum -= val
            self.high_sum += val
            self.low_size -= 1
            self.high_size += 1
            self.prune(self.low, True)
        elif self.low_size < self.high_size:
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)
            self.high_sum -= val
            self.low_sum += val
            self.high_size -= 1
            self.low_size += 1
            self.prune(self.high, False)

    def add(self, num):
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
            self.low_sum += num
            self.low_size += 1
        else:
            heapq.heappush(self.high, num)
            self.high_sum += num
            self.high_size += 1
        self.rebalance()

    def remove(self, num):
        self.delayed[num] += 1
        if num <= -self.low[0]:
            self.low_sum -= num
            self.low_size -= 1
            if num == -self.low[0]:
                self.prune(self.low, True)
        else:
            self.high_sum -= num
            self.high_size -= 1
            if self.high and num == self.high[0]:
                self.prune(self.high, False)
        self.rebalance()

    def get_cost(self):
        median = -self.low[0]
        cost_low = median * self.low_size - self.low_sum
        cost_high = self.high_sum - median * self.high_size
        return cost_low + cost_high


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)
        
        # 1. Precalculate conversion costs for all windows of size x
        median_tracker = SlidingWindowMedian(x)
        
        for i in range(n):
            median_tracker.add(nums[i])
            if i >= x:
                median_tracker.remove(nums[i - x])
            if i >= x - 1:
                cost[i - x + 1] = median_tracker.get_cost()

        # 2. Dynamic Programming
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option 1: Do not include a subarray ending at index i - 1
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Include a subarray of size x ending at index i - 1
                if i >= x:
                    dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + cost[i - x])

        return dp[n][k]