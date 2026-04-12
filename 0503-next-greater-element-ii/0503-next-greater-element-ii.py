class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n):
            curr = nums[i%n]
            while stack and nums[stack[-1]]<curr:
                idx = stack.pop()
                res[idx] = curr
            if i<n:
                stack.append(i)
        return res

# Approach
# Create a result array initialized with -1.

# Use a stack to store indexes of elements.

# Traverse the array twice (2 * n) to simulate circular behavior.

# For each element:

# While stack is not empty and current number is greater than stack top:

# Pop index and update its result.
# Push index into stack only during first pass.