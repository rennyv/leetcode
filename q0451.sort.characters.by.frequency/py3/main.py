class Solution:
    def frequencySort(self, s: str) -> str:
        ls = {}

        for i in s:
            if i in ls:
                ls[i] += 1
            else:
                ls[i] = 1
        
        ls = {k: v for k, v in sorted(ls.items(), key=lambda item: item[1])}

        s  = ""
        for j,v in ls.items():
            s+=(j*v)
        s = s[::-1]
        return s

def test_ex1():
    s = "tree"    
    ans = "eetr"

    sol = Solution()

    print(ans)
    print(sol.frequencySort(s))


def test_ex2():
    s = "cccaaa"    
    ans = "aaaccc"

    sol = Solution()

    print(ans)
    print(sol.frequencySort(s))

test_ex1()