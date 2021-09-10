class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while(n != 0):
            if n & 1 == 1: #if the right most bit is 1
                count += 1
            
            n = n >> 1
        return count 


def test_ex1():
    n = 11
    output = 3
    sol = Solution()
    assert output == sol.hammingWeight(n)

    
def test_ex2():
    n = int('0b00000000000000000000000010000000', 2)
    output = 1
    sol = Solution()
    assert output == sol.hammingWeight(n)

def test_ex2():
    n = int('0b11111111111111111111111111111101', 2)
    output = 31
    sol = Solution()
    assert output == sol.hammingWeight(n)