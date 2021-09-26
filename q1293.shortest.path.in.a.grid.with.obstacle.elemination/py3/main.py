import collections

class Solution:
    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        
        queue = collections.deque([(0,0,k)])
        seen = set()
        seen.add((0,0,k))
        
        ans = 0

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            for _ in range(len(queue)):
                i, j , curr_k = queue.popleft()

                if i == m - 1 and j == n -1:
                    return ans
                
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]

                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            if curr_k > 0 and (ni,nj,curr_k-1) not in seen:
                                queue.append((ni,nj,curr_k-1))
                                seen.add((ni,nj,curr_k-1))
                        else:
                            if (ni,nj,curr_k) not in seen:
                                queue.append((ni,nj,curr_k))
                                seen.add((ni,nj,curr_k))


            ans += 1

        return -1

def test_ex1():
    grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]], 
    k = 1
    ans = 6

    sol = Solution()
    assert ans == sol.shortestPath(grid, k)

def test_ex2():
    grid = [[0,1,1],
        [1,1,1],
        [1,0,0]],
    k = 1
    ans = -1

    sol = Solution()
    assert ans == sol.shortestPath(grid, k)

test_ex1()