import bisect

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        l = 0
        r= len(nums1)

        total_length = len(nums1)+len(nums2)
        half = total_length // 2

        while True:
            partition1 = (l+r) // 2
            partition2 = half - partition1

            num1_right = nums1[partition1] if partition1 < len(nums1) else float("infinity")
            num1_left = nums1[partition1-1] if partition1 > 0 else float("-infinity")
            num2_right = nums2[partition2] if partition2 < len(nums2) else float("infinity")
            num2_left = nums2[partition2-1] if partition2 > 0 else float("-infinity")

            if num1_left <= num2_right and num2_left <= num1_right:
                if total_length % 2:
                    return min(num1_right, num2_right)
                else:
                    return (min(num1_right, num2_right) + max(num1_left, num2_left)) / 2
            elif num1_left > num2_right:
                r = partition1
            else:
                l = partition1+1




            




