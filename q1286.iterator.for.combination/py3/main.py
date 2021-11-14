from typing import deque


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.all_combinations = deque([])
        self.characters = characters
        self.combinationLength = combinationLength
        if len(characters) > 0 and combinationLength > 0:
            self.generateComb(0, [])
    
    def next(self) -> str:
        if self.all_combinations:
            return self.all_combinations.popleft()       

    def hasNext(self) -> bool:
        return len(self.all_combinations) != 0

    def generateComb(self, start, comb):
        if len(comb) == self.combinationLength:
            self.all_combinations.append(''.join(comb))
            return

        for i in range(start, len(self.characters)):
            if self.characters[i] not in comb:
                comb.append(self.characters[i])
                self.generateComb(i + 1, comb)
                comb.pop()


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()