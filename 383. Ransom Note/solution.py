class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## probably need to use a dictionary

        counts = dict()
        for letter in magazine: #O(n)
            counts[letter] = counts.get(letter,0) + 1

        for letter in ransomNote: #O(m)
            if letter not in counts: #O(cardinaility of n)
                return False
            if counts[letter] == 0:
                return False
            counts[letter] -= 1
        
        return True
            