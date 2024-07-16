class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        return list(map(lambda a: a + extraCandies >= max(candies), candies))
    
       