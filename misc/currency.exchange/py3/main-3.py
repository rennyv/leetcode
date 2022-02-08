from collections import defaultdict, deque
from locale import currency

class Solution():
    def ConvertRate(self, start, end, data):
        #Create edges
        exchange = defaultdict(list)

        for s, e, r in data:
            exchange[s].append((e, r))
            exchange[e].append((s, 1/r))

        #find all routes
        ans = {}
        q = deque()
        q.append((start, 1, []))

        while q:
            currency, rate, visited = q.popleft()
            if currency in visited: continue

            visited.append(currency)

            for c, r in exchange[currency]:
                if not c in visited:
                    if end == c:
                        ans[rate*r] = visited + [c]
                        continue
                q.append((c, rate*r, visited))

        #find best convert
        maxrate = max(ans.keys())
        return maxrate, ans[maxrate]


def test_ex1():
    start = 'GBP'
    end = 'AUD'
    data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
    ans = (1.88, ["GBP", "JPY", "USD", "AUD"])

    sol = Solution()
    v = sol.ConvertRate(start, end, data)

    assert ans[0] == round(v[0], 2)
    assert ans[1] == v[1]

def test_ex2():
    start = 'GBP'
    end = 'AUD'
    data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070), ("GBP","AUD", 1.8)]
    ans = (1.88, ["GBP", "JPY", "USD", "AUD"])

    sol = Solution()
    v = sol.ConvertRate(start, end, data)
    
    assert ans[0] == round(v[0],2)
    assert ans[1] == v[1]

def test_ex3():
    start = 'GBP'
    end = 'AUD'
    data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070), ("GBP","AUD", 1.9)]
    ans = (1.9, ["GBP", "AUD"])

    sol = Solution()
    v = sol.ConvertRate(start, end, data)
    
    assert ans[0] == round(v[0],2)
    assert ans[1] == v[1]

test_ex2()