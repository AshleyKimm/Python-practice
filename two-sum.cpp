#include <vector>
#include <unordered_map>
using namespace std;

// two-pass hash table
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> numMap;

            for (int i{}; i < nums.size(); i++) {
                numMap[nums[i]] = i;
            }

            for (int i{}; i < nums.size(); i++) {
                int comp = nums[i] - target;
                if (numMap.count(comp) && comp != i) return {i, numMap[comp]};
            }
        }
    };