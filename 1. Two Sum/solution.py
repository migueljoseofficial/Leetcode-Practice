class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a seen dictionary 
        seen = {}
        # loop through the list
        for i, num in enumerate(nums):
            # find a value that can lead to our target
            remains = target - num

            #if that value is in our seen list, then we have found the indices.
            if remains in seen:
                return[i, seen[remains]]
            # add that value to our seen list
            else:
                seen[num] = i