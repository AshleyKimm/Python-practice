class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            unordered_set<char> set;
            int maxLen{}, left{};
      
            for (int right{}; right < s.length(); right++) {
                if (!set.count(s[right])) {
                    maxLen = max(maxLen, right - left + 1);
                } else {
                    while (set.count(s[right])) {
                        set.erase(s[left]);
                        left ++;
                    }
                }
                set.insert(s[right]);
            }
            return maxLen;
        }
    };