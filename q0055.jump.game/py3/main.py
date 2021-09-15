class Solution:
   def canJump(self, nums) -> bool:
      m = 0
      for i in range(0, len(nums)):            
         m = max(m-1, nums[i])
         if i == len(nums) - 1:
            return True
         if m == 0:
            return False
      return False
            

        

def test_ex1():
   nums = [2,3,1,1,4]

   sol = Solution()
   assert sol.canJump(nums) 

def test_ex2():
   nums = [3,2,1,0,4]

   sol = Solution()
   assert not sol.canJump(nums)

def test_ex3():
   nums = [3]

   sol = Solution()
   assert sol.canJump(nums)

def test_ex4():
   nums = [0]

   sol = Solution()
   assert sol.canJump(nums)

def test_ex4():
   nums = [2,0,0]

   sol = Solution()
   assert sol.canJump(nums)

test_ex2()