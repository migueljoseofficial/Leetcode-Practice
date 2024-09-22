class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        totalJewels = 0

        #goes through every type of stone
        for x in stones: ##O(n)
            ## checks if each stone is a jewel
            if x in jewels: #O(m) 
                totalJewels += 1
        

        return totalJewels