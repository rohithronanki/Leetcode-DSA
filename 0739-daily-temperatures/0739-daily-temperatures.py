class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t=temperatures
        res = [0]*len(t)
        stack=[]
        for i in range(len(t)):
            if not stack:
                stack.append(i)
                continue
            else:
                while stack and t[stack[-1]]<t[i]:
                    res[stack[-1]] = i-stack[-1]
                    stack.pop()
                stack.append(i)
        return res

# Approach
# Initialize:
# res array with 0s
# Empty stack (stores indices)
# Traverse temperatures:
# While current temp > temp at stack top:
# Pop index
# Calculate days difference
# Push current index into stack
# Remaining indices → no warmer day → stay 0

        