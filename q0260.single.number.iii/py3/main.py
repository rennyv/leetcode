from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for n in nums:
            if n in s: s.remove(n)
            else: s.add(n)
        return s
    
def test_ex1():
    nums = [1,2,1,3,2,5]
    ans = [5,3]

    sol = Solution()
    print(ans)
    print(sol.singleNumber(nums))

def test_ex2():
    nums = [-1, 0]
    ans = [-1,0]

    sol = Solution()
    print(ans)
    print(sol.singleNumber(nums))

def test_ex3():
    nums = [1, 0]
    ans = [1,0]

    sol = Solution()
    print(ans)
    print(sol.singleNumber(nums))