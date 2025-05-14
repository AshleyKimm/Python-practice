class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in charSet:
                maxLen = max(maxLen, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
            charSet.add(s[right])
        return maxLen