from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        SIZE = 26  # 26 letters in the alphabet
        trie = [[0] * SIZE]  # we use list to mimic the trie tree
        count = [0]  # the number of words ending at node i
        for word in words:
            word = sorted(set(word))
            if len(word) <= 7:  # longer words are never valid
                # insert into trie
                node = 0
                for letter in word:
                    i = ord(letter) - ord('a')
                    if trie[node][i] == 0:  # push empty node
                        trie.append([0] * SIZE)
                        count.append(0)
                        trie[node][i] = len(trie) - 1
                    node = trie[node][i]
                count[node] += 1

        # search for valid words
        def dfs(node, has_first):
            total = count[node] if has_first else 0
            for letter in puzzle:  # catch puzzle from outside environment
                i = ord(letter) - ord('a')
                if trie[node][i]:
                    total += dfs(trie[node][i], has_first or letter == puzzle[0])
            return total

        result = []
        for puzzle in puzzles:
            result.append(dfs(0, False))
        return result


def test_ex1():
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    ans = [1,1,3,2,4,0]

    sol = Solution()
    assert ans == sol.findNumOfValidWords(words, puzzles)


def test_ex2():
    words = ["apple","pleas","please"]
    puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
    ans =  [0,1,3,2,0]

    sol = Solution()
    assert ans == sol.findNumOfValidWords(words, puzzles)

test_ex1()