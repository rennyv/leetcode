class Solution:
    def letterCasePermutation(self, s: str):
        if len(s) <= 1:
            return list({s.lower(), s.upper()})

        s_except_last = s[:-1]
        s_last = s[-1]
        
		# Get all permutations of the string except the last character
        lcpermutations_except_last = self.letterCasePermutation(s_except_last)
        
		# Initialize a set to avoid adding already generated permutations
        permutations = set()
        for lcp_except_last in lcpermutations_except_last:
            permutation1 = lcp_except_last + s_last.lower()
            permutation2 = lcp_except_last + s_last.upper()
            permutations.add(permutation1)
            permutations.add(permutation2)
        
        return list(permutations)

        


def test_ex1():
    sol = Solution()
    s = "a2b3"
    print(sol.letterCasePermutation(s))

test_ex1()