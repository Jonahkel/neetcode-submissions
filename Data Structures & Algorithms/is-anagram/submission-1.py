class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letters = {}
        for let in s:
            if let not in letters: 
                letters[let] = 1
            else:
                letters[let] += 1
        for let in t:
            count = letters.get(let, 0)
            if count == 0:
                return False
            letters[let] -= 1
        return True 