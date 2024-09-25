class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       
        #can use hashmap.
        counts = {}
        num = 0
        balloon = "balloon"
        
        

        for letter in text:
            if letter not in balloon:
                pass
            counts[letter] = counts.get(letter, 0) + 1

        #check if all the required letterse are present
        if set(balloon) - counts.keys():
            return 0

        return min(counts["b"], counts["a"], counts["l"]//2, counts["o"]//2, counts["n"])