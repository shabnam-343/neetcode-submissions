class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n-1
        left_max = height[left]
        right_max = height[right]
        water_stored = 0

        while left<right :
            if height[left]<height[right]:
                if left_max<height[left]:
                    left_max = height[left]
                else:
                    water_stored+=left_max - height[left]
                left+=1
            else:
                if right_max<height[right]:
                    right_max = height[right]
                else:
                    water_stored += right_max-height[right]
                right-=1
                
        return water_stored