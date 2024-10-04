class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        lowest = nums[0]
        for x in nums:
            if abs(x) < abs(lowest):
                lowest = x
            if abs(x) == abs(lowest):
                if x > lowest:
                    lowest = x
    
            
        

        return lowest