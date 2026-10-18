class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        result = 0
        # Determine sign and work with absolute value to avoid Python's negative modulo quirk
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before actually multiplying and adding
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
                return 0
            
            result = (result * 10) + pop
            
        return result * sign