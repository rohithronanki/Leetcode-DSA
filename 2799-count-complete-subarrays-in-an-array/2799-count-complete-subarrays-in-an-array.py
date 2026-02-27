class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        left=0
        set1=set(nums)
        Hashmap={}
        for right in range(len(nums)):
            Hashmap[nums[right]] = Hashmap.get(nums[right],0)+1
            while len(set1)==len(Hashmap):
                count+=len(nums) - right  # all subarrays from left→right to end are valid
                Hashmap[nums[left]] -= 1
                if Hashmap[nums[left]] == 0:
                    del Hashmap[nums[left]]
                left+=1

        return count

