def lengthOfLongestSubstring(s: str) -> int:
    maxLen = 0
    left = 0
    charSet = set()

    for right in range(len(s)):
        if s[right] not in charSet:
            maxLen = max(max, right - left)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
        charSet.add(s[right])
    return maxLen