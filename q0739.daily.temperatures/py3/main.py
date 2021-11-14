from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums = [0 for x in temperatures]
        
        stack = [(temperatures[0],0)]
        
        for i,temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                nums[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                while stack and temp > stack[-1][0]:
                    nums[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                
            stack.append((temp,i))
        return nums  



def test_ex1():
    temperatures = [73,74,75,71,69,72,76,73]
    ans = [1,1,4,2,1,1,0,0]

    sol = Solution()
    assert ans == sol.dailyTemperatures(temperatures)

def test_ex2():
    temperatures = [30,40,50,60]
    ans = [1,1,1,0]

    sol = Solution()
    assert ans == sol.dailyTemperatures(temperatures)

def test_ex3():
    temperatures = [30,60,90]
    ans = [1,1,0]

    sol = Solution()
    assert ans == sol.dailyTemperatures(temperatures)
