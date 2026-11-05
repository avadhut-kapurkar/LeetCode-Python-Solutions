class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num in arr1:
            valid = True

            for x in arr2:
                if abs(num - x) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count