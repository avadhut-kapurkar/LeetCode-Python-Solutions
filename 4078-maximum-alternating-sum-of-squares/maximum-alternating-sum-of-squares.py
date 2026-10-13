from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        k = (n + 1) // 2

        ans = 0

        for i in range(k):
            ans += nums[n - 1 - i] ** 2

        for i in range(n - k):
            ans -= nums[i] ** 2

        return ans