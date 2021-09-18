class Solution:
    def intersect(self, nums1, nums2):
        if(len(nums1)>len(nums2)):
            return self.intersect(nums2, nums1)

        d = {}
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        intersect = []
        for num in nums2:
            if num in d:
                count = d[num]
            else:
                count = 0
            if count > 0:
                intersect.append(num)
                d[num] -= 1
        return intersect

def test_ex1():
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    ans = [2,2]
    sol = Solution()

    assert ans == sol.intersect(nums1,nums2)

def test_ex2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    ans = [4,9]
    sol = Solution()

    assert ans == sol.intersect(nums1,nums2)

