class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def comb(start,currtarget,sub):
            if currtarget==0:
                res.append(sub[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i] <= currtarget:
                    sub.append(candidates[i])
                    comb(i,currtarget-candidates[i],sub)
                    sub.pop()
        comb(0,target,[])
        return res

        