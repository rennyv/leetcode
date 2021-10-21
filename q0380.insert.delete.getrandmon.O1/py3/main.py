import random

class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            self.arr.append(val)
            return True
        return False        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.arr.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)



        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def test_ex1():
    rs = RandomizedSet()

    assert rs.insert(1)
    assert not rs.remove(2)
    assert rs.insert(2)
    print(rs.getRandom())
    assert rs.remove(1)
    assert not rs.insert(2)
    assert 2 == rs.getRandom()

test_ex1()

