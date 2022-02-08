#Find the *best* rate

from collections import defaultdict, deque


class Solution():
    def ConvertRate(self, start, end, data):
        #Create graph nodes
        rates = defaultdict(list)

        for t, f, rate in data:
            rates[t].append((f, rate))
            rates[f].append((t, 1/rate))

        #Search through nodes
        ans = []
        visited = set()
        
        q = deque()
        q.append((start, 1))

        while q:
            current_currency, current_rate = q.popleft()
            if current_currency in visited: continue

            visited.add(current_currency)

            for currency, rate in rates[current_currency]:
                if not currency in visited:
                    if currency == end:
                        return current_rate * rate
                    q.append((currency, rate * current_rate))



        #return best rate
        pass






def test_ex1():
    start = 'GBP'
    end = 'AUD'
    data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
    ans = 1.88

    sol = Solution()
    assert ans == round(sol.ConvertRate(start, end, data), 2)

test_ex1()