class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = []

        while sum > 0 and num > 0:
            digit = min(9, sum)
            ans.append(str(digit))
            sum -= digit
            num -= 1

        ans.extend(["0"] * num)

        return "".join(ans)