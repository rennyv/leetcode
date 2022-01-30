from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Hash Table, O(n)
        found = set()
        for i in nums:
            if i in found:
                return True
            found.add(i)
        return False


def test_ex1():
    nums = [1,2,3,1]
    sol = Solution()

    assert sol.containsDuplicate(nums)


def test_ex2():
    nums = [1,2,3,4]
    sol = Solution()

    assert not sol.containsDuplicate(nums)

def test_ex3():
    nums = [1,1,1,3,3,4,3,2,4,2]
    sol = Solution()

    assert sol.containsDuplicate(nums)