import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def count_ways(arr):
            
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            
       
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
           
            ways_to_interleave = math.comb(len(left) + len(right), len(left))
            
            total_ways = (ways_to_interleave * count_ways(left) * count_ways(right)) % MOD
            
            return total_ways
            
        
        return (count_ways(nums) - 1) % MOD