class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        index = {}
        for c in s:
            if c in index:
                index[c] += 1
            else:
                index[c] = 1
        for c in t:
            if c in index:
                index[c] -= 1
            else:
                return False
        for ind in index.values():
            if(ind != 0):
                return False
        return True