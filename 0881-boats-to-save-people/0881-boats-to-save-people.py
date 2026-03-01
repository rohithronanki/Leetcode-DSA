class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        left=0
        right=len(people)-1
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                boat+=1
                left+=1
                right-=1
            else:
                right-=1
                boat+=1
        return boat


        