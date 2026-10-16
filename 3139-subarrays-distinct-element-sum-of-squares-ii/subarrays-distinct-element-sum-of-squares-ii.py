class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
            # If the current range is completely inside the query range
            if ql <= l and r <= qr:
                length = r - l + 1
                # Update sum2: (x + val)^2 = x^2 + 2*val*x + val^2
                sum2[node] = (sum2[node] + 2 * val * sum1[node] + val * val * length) % MOD
                # Update sum1: x + val
                sum1[node] = (sum1[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return

            # Push down the lazy values to children
            mid = (l + r) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            
            if lazy[node]:
                l_val = lazy[node]
                
                # Apply to left child
                len_left = mid - l + 1
                sum2[left_child] = (sum2[left_child] + 2 * l_val * sum1[left_child] + l_val * l_val * len_left) % MOD
                sum1[left_child] = (sum1[left_child] + l_val * len_left) % MOD
                lazy[left_child] = (lazy[left_child] + l_val) % MOD
                
                # Apply to right child
                len_right = r - mid
                sum2[right_child] = (sum2[right_child] + 2 * l_val * sum1[right_child] + l_val * l_val * len_right) % MOD
                sum1[right_child] = (sum1[right_child] + l_val * len_right) % MOD
                lazy[right_child] = (lazy[right_child] + l_val) % MOD
                
                lazy[node] = 0

            # Recurse for children
            if ql <= mid:
                update(left_child, l, mid, ql, qr, val)
            if qr > mid:
                update(right_child, mid + 1, r, ql, qr, val)

            # Recompute current node's sums from its children
            sum1[node] = (sum1[left_child] + sum1[right_child]) % MOD
            sum2[node] = (sum2[left_child] + sum2[right_child]) % MOD

        last = {}
        total_ans = 0
        
        for i, num in enumerate(nums):
            # Calculate the range to update: from the element's last seen index + 1 to the current index i
            start = last.get(num, -1) + 1
            
            # Update the distinct counts for all subarrays ending at index i and starting between `start` and `i`
            update(1, 0, n - 1, start, i, 1)
            
            # The root node (1) holds the sum of squares of distinct counts for all subarrays ending at current index i
            total_ans = (total_ans + sum2[1]) % MOD
            
            # Record the current index as the latest occurrence of the element
            last[num] = i

        return total_ans