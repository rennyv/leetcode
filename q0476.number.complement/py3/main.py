class Solution:
    def findComplement(self, num: int) -> int:
        #convert to bin
        bin_str = bin(num).replace("0b","")

        #invert bin
        comp_str = "".join(["0" if int(digit) else "1" for digit in bin_str])
        
        #convert to base10
        return int(comp_str, 2)


def test_ex1():
    num = 5
    ans = 2

    sol = Solution()
    assert ans == sol.findComplement(num)

def test_ex2():
    num = 1
    ans = 0

    sol = Solution()
    assert ans == sol.findComplement(num)
  