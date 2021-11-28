from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.ranks = [0] * (n+1)
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
        elif self.ranks[root_x] > self.ranks[root_y]:
            self.parents[root_y] = root_x
        else:
            self.parents[root_x] = root_y
            self.ranks[root_y] += 1
        
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_num = max(nums)
        uf = UnionFind(max_num)
        is_prime = [True for _ in range(max_num+1)]
        for num in range(2, max_num+1):
            if is_prime[num]:
                for composite in range(num, max_num+1, num):
                    if composite != num:
                        is_prime[composite] = False
                    if composite in nums_set:
                        uf.union(num, composite)
        
        cluster_to_cnt = defaultdict(int)
        for num in nums:
            cluster_to_cnt[uf.find(num)] += 1
        return max([cnt for _, cnt in cluster_to_cnt.items()])


def test_ex1():
    nums = [4,6,15,35]
    ans = 4

    sol = Solution()
    assert ans == sol.largestComponentSize(nums)

def test_ex2():
    nums = [20,50,9,63]
    ans = 2

    sol = Solution()
    assert ans == sol.largestComponentSize(nums)