class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={']':'[','}':'{',')':'('}
        length = len(s)
        if length%2 != 0:
            return False 
        for char in s:
            if char in mapping:  # Closing bracket
                if not st or st.pop() != mapping[char]:
                    return False
            else:  # Opening bracket
                st.append(char)

        return len(st) == 0



        