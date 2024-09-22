class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        totalJewels = 0

        # set for optimization 
        s = set(jewels)
        #goes through every type of stone
        for x in stones: ##O(n)
            ## checks if each stone is a jewel
            if x in s: #O(1)
                totalJewels += 1
        
        #O(n + m)
        return totalJewels