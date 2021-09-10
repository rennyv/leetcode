class Solution:
    def reverseBits(self, n: int) -> int:
        a = "{:032b}".format(n)
        b = a[::-1]
        return int(b,2)


def test_ex1():
    n = int('0b00000010100101000001111010011100', 2)
    output = 964176192
    sol = Solution()
    assert output == sol.reverseBits(n)

test_ex1()
