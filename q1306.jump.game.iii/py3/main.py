from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])

        return False

def test_ex1():
    arr = [4,2,3,0,3,1,2]
    start = 5

    sol = Solution()
    assert sol.canReach(arr, start)

def test_ex2():
    arr = [4,2,3,0,3,1,2]
    start = 0

    sol = Solution()
    assert sol.canReach(arr, start)

def test_ex3():
    arr = [3,0,2,1,2]
    start = 2

    sol = Solution()
    assert not sol.canReach(arr, start)

def test_ex4():
    arr = [0,1]
    start = 1

    sol = Solution()
    assert sol.canReach(arr, start)
    