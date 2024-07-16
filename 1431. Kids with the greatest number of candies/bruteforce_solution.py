class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        bool_candies = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                bool_candies.append(True)
            else:
                bool_candies.append(False)

        return bool_candies
