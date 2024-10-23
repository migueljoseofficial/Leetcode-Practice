class Solution:
    def maxArea(self, height: List[int]) -> int:
        #difference between left and right pointer is the width.
        def find_width(l, r):
            return r - l

        def find_area(width, height):
            return width * height
        #can only create a container of the smaller length of the line. (take the min)

        l = 0 
        r = len(height) - 1
        highest_area = 0
        while l <= r:

            #find the length and area to check
            width = find_width(l, r)
            lower_height = min(height[l],height[r])
            area = find_area(width, lower_height)
            print(f"width: {width}")
            print(f"height {height[l]}\n")
            
            # reaplce the highest area if we find a better one
            if area > highest_area:
                highest_area = area
            
            # we only want to move the poitner that is lower
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return highest_area




