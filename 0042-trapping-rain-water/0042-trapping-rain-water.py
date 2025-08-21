class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height)==0:
            return 0
        
        left,right=0,len(height)-1
        max_left=height[0]
        max_right=height[-1]

        water=0
        while left<right:

            if max_left < max_right:
                water += max_left-height[left]
                left += 1

            else:
                water += max_right-height[right]
                right -= 1
            
            max_left = max(max_left,height[left])
            max_right = max(max_right,height[right])

        return water


