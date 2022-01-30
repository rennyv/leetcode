import heapq


def findMaxProduct(arr):
    h=[-1,-1, -1]
    heapq.heapify(h)
    ans = []
    for i in range(len(arr)):
        heapq.heappushpop(h,arr[i])
        if i < 2:
            ans.append(-1)
        else:
            result = 1
            for j in range(len(h)):
                result = result * h[j]
            ans.append(result)

    return ans

def test_ex1():
    arr = [2,1,2,1,2]
    output = [-1,-1,4,4,8]

    assert output == findMaxProduct(arr)

test_ex1()