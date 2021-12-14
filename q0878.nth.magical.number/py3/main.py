 from fractions import gcd

class Solution:
    def nthMagicalNumber(self, N, A, B):
        lcm, Q = A*B//gcd(A,B), 10**9 + 7
        cand = sorted([A*i for i in range(1,lcm//A)] + [B*i for i in range(1,lcm//B+1)])
        m = len(cand)
        return (cand[(N-1)%m] + lcm*((N-1)//m)) % Q