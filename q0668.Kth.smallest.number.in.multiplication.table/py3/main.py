#Binary Search
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left=1
        right=m*n

        while left<right:
            mid=(left+right)//2
            if(self.check(mid, m, n, k)):
                right=mid
            else:
                left=mid+1
        return right
    
    def check(self, mid, m, n, k):
        elements=0
        for i in range(1,m+1):
            current_ele_count = min(mid//i,n)
            elements+=current_ele_count
        return elements>=k


def test_ex1():
     m = 3
     n = 3
     k = 5

     ans = 3

     sol = Solution()
     assert ans == sol.findKthNumber(m,n,k)

def test_ex2():
     m = 3
     n = 3
     k = 5

     ans = 3

     sol = Solution()
     assert ans == sol.findKthNumber(m,n,k)

test_ex1()
