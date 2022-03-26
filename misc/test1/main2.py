
from collections import defaultdict


def solution(S):   
    L = len(S)
    
    #if the length is less than 0
    if L < 3:
        return 0
    
    #if you can't divide equally don't need to run the rest of it
    totalA = S.count('a')
    if (totalA % 3) > 0:
        return 0
    
    #Only worried about when we have a third
    third = totalA//3

    counter=0
    #a bit of caching?
    thirdACount = defaultdict(int)
    for i in range(0,L-2):
        sub1 = S[0:i+1]
        sub1_c =  sub1.count('a')
        if sub1_c != third:
            continue
        for j in range(i+1,L-1):
            if j+1 in thirdACount.keys():
                sub3_c = thirdACount[j+1]
            else:
                sub3_c = S[j+1:].count('a')
                thirdACount[j+1]=sub3_c
            if sub1_c == sub3_c:
                counter += 1

    return counter


def test_ex1():
    s = "babaa"
    ans = 2
    assert ans == solution(s)

def test_ex2():
    s = "ababa"
    ans = 4

    assert ans == solution(s)

def test_ex3():
    s = "bbbbb"
    ans = 6

    assert ans == solution(s)


test_ex1()