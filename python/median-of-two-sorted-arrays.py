class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)

        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[(len(nums1)//2) - 1]) / 2.0
        return nums1[len(nums1)//2]
        