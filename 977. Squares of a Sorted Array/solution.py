class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        new_list = list(map(lambda x: x * x, nums))

        i = 0
        j = len(nums) - 1
        sorted_list = []
        while i <= j:
            if new_list[j] >= new_list[i]:
                sorted_list.append(new_list[j])
                j-=1
            else:
                sorted_list.append(new_list[i])
                i+=1

        sorted_list.reverse()

        return sorted_list
