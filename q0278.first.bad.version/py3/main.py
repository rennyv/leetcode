# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def isBadVersion(self, version):
        return version == 4

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (right + left) // 2
            print( left, right, mid)
            isBad = self.isBadVersion(mid)
            if isBad:
                right = mid - 1
            else:
                left = mid + 1
        return left

def test_ex1():
	sol = Solution()
	num = 5
	assert sol.firstBadVersion(num) == 4


sol = Solution()
num = 5
sol.firstBadVersion(num)
