class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #one edge case is length
        if len(s) != len(t):
            return False

        #can also use a dictionary
        count_t = dict()
        count_s = dict()

        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1
        for letter in s:
            count_s[letter] = count_s.get(letter, 0) + 1

        return count_t == count_s