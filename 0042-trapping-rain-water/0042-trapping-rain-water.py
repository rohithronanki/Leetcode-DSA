class Solution:
    def trap(self, height: List[int]) -> int:
        #quantity of water stored = min(leftmax,rightmax)-arr[i]
        leftmax=0
        left=0
        right=len(height)-1
        rightmax=0
        total=0
        while left<right:
            if height[left]<=height[right]:
                if leftmax > height[left]:
                    total+= leftmax-height[left]
                else:
                    leftmax = height[left]
                left+=1
            else:
                if rightmax > height[right]:
                    total+= rightmax-height[right]
                else:
                    rightmax = height[right]
                right-=1
        return total
                
