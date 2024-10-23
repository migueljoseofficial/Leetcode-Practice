class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #want to use two pointers
        l = 0
        r = len(numbers) -1 

        while l <= r:
            test = numbers[l] + numbers[r]
            #this is just right and we return
            if test == target:
                return [l+1,r+1]
            #want to get a lower test number
            elif test > target:
                r -=1
            # want to get a higher test number
            elif test < target:
                l+= 1
