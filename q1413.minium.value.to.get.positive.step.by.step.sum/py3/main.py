from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int: 
        Sum, ans = 0, 0
        for num in nums:
            Sum += num
            ans = min(ans, Sum)
        return -ans + 1