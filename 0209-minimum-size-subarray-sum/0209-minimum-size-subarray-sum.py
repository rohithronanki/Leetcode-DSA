class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowsum=0 #using sliding window
        left=0
        minlength=float('inf')
        for right in range(len(nums)):
            windowsum+=nums[right]
            while windowsum >= target:
                minlength = min(minlength, right-left+1)
                windowsum -= nums[left]
                left+=1
        return minlength if minlength != float('inf') else 0
