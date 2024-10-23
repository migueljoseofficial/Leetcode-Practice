class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we can easiy do a two pointer solution to check for this.

        #edge case if a string is empty
        if not s:
            return True

        l = 0
        r = len(s) -1


        while l < r:
            #most only consider the spaces where there are letters
            while l < r and not s[l].isalnum(): l+=1
            while l < r and not s[r].isalnum(): r-=1

            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True