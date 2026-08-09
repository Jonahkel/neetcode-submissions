class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        idx1 = 0
        idx2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 += 1
            else:
                merged.append(nums2[idx2])
                idx2 += 1
        while idx1 < len(nums1):
            merged.append(nums1[idx1])
            idx1 += 1
        while idx2 < len(nums2):
            merged.append(nums2[idx2])
            idx2 += 1
        
        if len(merged) % 2 == 0:
            l_med = merged[len(merged)//2 - 1]
            r_med = merged[len(merged)//2]
            return (l_med + r_med)/2
        else:
            return merged[len(merged) // 2]
