# ans?: https://leetcode.com/discuss/interview-question/483660/google-phone-currency-conversion


# Question
# Paramenters:

# array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
# an array containing a 'from' currency and a 'to' currency
# Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
# Your return value should be a number.

# Example:
# You are given the following parameters:

# Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
# To/From currency ['GBP', 'AUD']
# Find the rate for the 'To/From' curency. In this case, the correct result is 1.89


from collections import defaultdict
from collections import deque

class Solution():
    def ConvertRate(self, start: str, end: str, data) -> float:
        #load data
        dict = defaultdict(list)
        for node in data:
            dict[node[0]].append([node[1], node[2]])
            dict[node[1]].append([node[0], 1.0 / node[2]])

        
        #find path to ans:
        queue = deque()
        queue.append((start, 1.0))
        visited = set()

        while queue:
            curr, num = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)

            if curr in dict:
                values = dict.get(curr)
                next = {}
                for val in values:
                    next[val[0]] = val[1]
                for key in next:
                    if key not in visited:
                        if key == end:
                            return num * next[key]
                        queue.append((key, num*next[key]))
        return -1            

def test_ex1():
    start = 'GBP'
    end = 'AUD'
    data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
    ans = 1.88

    sol = Solution()
    assert ans == round(sol.ConvertRate(start, end, data), 2)

test_ex1()
    
    

