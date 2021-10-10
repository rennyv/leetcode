class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        rng = right - left + 1

        step, shift = 2, 0
        res = 0
        while left and right:
            if not (left & 1) or not (right & 1) or (step ** shift) < rng:
                shift += 1
            else:
                res |= 1 << shift
                shift += 1
            left >>= 1
            right >>= 1
            
        return res