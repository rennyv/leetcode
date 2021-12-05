from typing import List

class StreamChecker:

    def __init__(self, words: List[str]):
        self.phrase = ''
        self.words = []
        
        for word in sorted(words,key = len):
            word_founded = False
            for _word in self.words:
                if word.endswith(_word):
                    word_founded = True
                    break
            if word_founded:
                continue
            self.words.append(word)       

    def query(self, letter: str) -> bool:
        self.phrase += letter
        
        return any([self.phrase.endswith(word) for word in self.words])     


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

def test_ex1():
    sol = StreamChecker(["cd", "f", "kl"])
    assert sol.query("a") == False
    assert sol.query("b") == False
    assert sol.query("c") == False
    assert sol.query("d")
    assert sol.query("e") == False
    assert sol.query("f")
    assert sol.query("g") == False
    assert sol.query("h") == False
    assert sol.query("i") == False
    assert sol.query("j") == False
    assert sol.query("k") == False
    assert sol.query("l") 

test_ex1()
