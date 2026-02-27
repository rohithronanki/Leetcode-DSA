class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        maxfreq=0
        Hashmap = {}
        result=0
        for right in range(len(s)):
            Hashmap[s[right]]= Hashmap.get(s[right],0)+1
            windowsize = right-left+1
            maxfreq = max(maxfreq, Hashmap[s[right]])
            while windowsize-maxfreq > k:
                Hashmap[s[left]] -= 1
                left+=1
                windowsize = right-left+1
            result = max(result, windowsize)
        
        return result

#windowsize-maxfreq = k 
    #    class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     left = 0 
    #     maxfreq=0
    #     Hashmap = {}
    #     freq=1
    #     for right in range(len(s)):
            
    #         windowsize = right-left+1
    #         if s[right] in Hashmap:
    #             freq+=1
    #             Hashmap[s[right]]= freq

    #         Hashmap[s[right]]= freq
    #         maxfreq = max(maxfreq, freq)
    #         if windowsize-maxfreq <= k:
    #             return windowsize


         