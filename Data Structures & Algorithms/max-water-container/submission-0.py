class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxi = 0

        while l < r :
            width = r-l
            current_height = min(heights[l],heights[r])
            area = width*current_height
            maxi = max(maxi,area)


            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
               
        return maxi
        