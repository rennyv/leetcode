#Input : test_list1 = [3, 8, 7], test_list2 = [5, 7, 3, 0, 1, 8]

#Output : [3, 5, 8, 7, 7, 3, 3, 0, 8, 1, 7, 8]
#Question if an array is empty what to do?

class Interweave():
    def __init__(self, s1, s2) -> None:
        self.s1 = s1
        self.s2 = s2

    def __iter__(self):
        self.p1 = 0
        self.p2 = 0
        self.count = 0
        return self
    
    def __next__(self):
        c = self.count + 1

        if (self.p1>=len(self.s1) and self.p2 >= len(self.s2)):
            raise StopIteration
        
        self.count = c
        if c % 2 == 1:
            v = self.s1[(self.p1 % len(self.s1))]
            self.p1 += 1
            return v
        v = self.s2[(self.p2 % len(self.s2))]
        self.p2 += 1
        return v




def test_ex1():
    test_list1 = [3, 8, 7]
    test_list2 = [5, 7, 3, 0, 1, 8]

    ans = [3, 5, 8, 7, 7, 3, 3, 0, 8, 1, 7, 8]

    a = []
    for i in Interweave(test_list1, test_list2):
        a.append(i)
    assert ans == a


def test_ex2():
    test_list1 = [3]
    test_list2 = [5, 7, 3, 0, 1, 8]

    ans = [3, 5, 3, 7, 3, 3, 3, 0, 3, 1, 3, 8]

    a = []
    for i in Interweave(test_list1, test_list2):
        a.append(i)
    assert ans == a

def test_ex3():
    test_list2 = [3]
    test_list1 = [5, 7, 3, 0, 1, 8]

    ans = [5, 3, 7, 3, 3, 3, 0, 3, 1, 3, 8]

    a = []
    for i in Interweave(test_list1, test_list2):
        a.append(i)
    assert ans == a

def test_ex4():
    test_list2 = []
    test_list1 = [5, 7, 3, 0, 1, 8]

    ans = [5, 3, 7, 3, 3, 3, 0, 3, 1, 3, 8]

    a = []
    for i in Interweave(test_list1, test_list2):
        a.append(i)
    assert ans == a



test_list1 = [3, 8, 7]
test_list2 = [5, 7, 3, 0, 1, 8]

test_list3 = [3, 4, 5]
test_list4 = [7, 8, 9]

for i in Interweave(test_list1, test_list2):
    print(i)
print("*****************")
for i in Interweave(test_list3, test_list4):
    print(i)