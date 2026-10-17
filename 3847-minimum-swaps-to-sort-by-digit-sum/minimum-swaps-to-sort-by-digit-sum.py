class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        ans = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]
                pos[nums[i]] = j
                pos[arr[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1

        return ans