class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0
        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        ans = 0
        while index < len(s) and s[index].isdigit():
            ans = ans * 10 + int(s[index])
            index += 1
        
            if ans * sign < -2**31:
                return -2**31 
            if ans * sign > 2**31 - 1:
                return (2**31 - 1) 
        return ans * sign

        