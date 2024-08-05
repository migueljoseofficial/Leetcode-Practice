class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def canPlace(flowerbed: List[int], index: int) -> bool:
            if (index == 0 or flowerbed[index - 1] == 0) and \
               (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                return True
            return False
        count = 0

        for index, flower in enumerate(flowerbed):
            can = canPlace(flowerbed, index)
            if flower == 0 and can == True:
                count += 1
                flowerbed[index] = 1


            
        if count >= n:
            return True
        else:
            return False