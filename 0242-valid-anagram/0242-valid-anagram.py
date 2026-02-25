class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # hashset=b=set()
        # for i in s:
        #     hashset.add(i)
        
        # for j in t:
        #     b.add(j)
        # print(hashset.issuperset(b))

        