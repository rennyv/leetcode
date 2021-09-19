class Solution:
    def addOperators(self, num, target):
        solutions = []
        L = len(num)

        def dfs(candidate, i, total, prev_add):
            if i == L and total == target: return solutions.append(candidate)
            for j in range(i+1, L+1):
                s = num[i:j]
                d = int(s)
                if num[i] == '0' and s!= '0': continue
                if not candidate:
                    dfs(s, j, d, d)
                else:
                    dfs(candidate + '+' + s, j, total + d, d)
                    dfs(candidate + '-' + s, j, total - d, -d)
                    dfs(candidate + '*' + s, j, total - prev_add + prev_add * d, prev_add * d)

        dfs('',0,0,0)
        return solutions


def test_ex1():
    num = "123"
    target = 6

    ans = ["1*2*3","1+2+3"]
    sol = Solution()
    print("ans", ans)
    print("sol",  sol.addOperators(num, target))


def test_ex2():
    num = "232"
    target = 8

    ans = ["2*3+2","2+3*2"]
    sol = Solution()
    print("ans", ans)
    print("sol", sol.addOperators(num,target))

def test_ex3():
    num = "105"
    target = 5

    ans = ["1*0+5","10-5"]
    sol = Solution()
    print("ans", ans)
    print("sol", sol.addOperators(num,target))

def test_ex4():
    num = "00"
    target = 0

    ans = ["0*0","0+0","0-0"]
    sol = Solution()
    print("ans", ans)
    print("sol", sol.addOperators(num,target))

def test_ex5():
    num = "3456237490"
    target = 9191

    ans = []
    sol = Solution()
    print("ans", ans)
    print("sol", sol.addOperators(num,target))

test_ex3()