class Solution:
    def combine(self, n: int, k: int):        
        result = []        
        def gen_comb(n, k, start, cur_comb):
            
            if k == len(cur_comb):
                # base case, also known as stop condition 
                result.append( cur_comb[::] )
                return
            
            else:
                # general case:
                # solve in DFS
                for i in range(start, n+1):
                    cur_comb.append( i )
                    gen_comb(n, k, i+1, cur_comb)
                    cur_comb.pop()
                return
        # ----------------------------------------------
        
        gen_comb( n, k, start=1, cur_comb=[] )
        return result


def test_ex1():
    sol = Solution()
    n=4
    k=2
    print(sol.combine(n,k))

def test_ex2():
    sol = Solution()
    n=5
    k=1
    print(sol.combine(n,k))

def test_ex3():
    sol = Solution()
    n=2
    k=2
    print(sol.combine(n,k))

test_ex1()