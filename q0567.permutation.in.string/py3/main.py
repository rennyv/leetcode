class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1len = len(s1)
        s1s = sorted(s1)
        for i in range(len(s2)-s1len+1):
            # print(i, s1s, sorted(s2[i:i+s1len]))
            if s1s == sorted(s2[i:i+s1len]):
                return True
        return False