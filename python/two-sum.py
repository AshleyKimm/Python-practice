
# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
                    

# two-pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numMap:
                return [i, numMap[comp]]
            numMap[nums[i]] = i

        return []
                    

        