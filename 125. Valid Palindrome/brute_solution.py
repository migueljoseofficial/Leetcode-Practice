class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if it's empty
        if not s:
            return True

        #lowercase everything
        s = s.lower()

        #take out all of the extra spaces and puncturation
        s = ''.join(e for e in s if e.isalnum())
    
        #see if it is a palindrome

        return s == s[::-1]
