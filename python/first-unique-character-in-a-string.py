class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if dict[char] == 1:
                return i
        return -1