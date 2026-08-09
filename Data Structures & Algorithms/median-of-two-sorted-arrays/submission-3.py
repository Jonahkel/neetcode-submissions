import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2): nums1, nums2 = nums2, nums1
        l1 = l2 = 0
        r1, r2 = len(nums1), len(nums2)

        total_length = len(nums1)+len(nums2)

        while l1 < r1:
            mid_idx = (l1+r1) // 2
            mid_value = nums1[mid_idx]
            small_idx = bisect.bisect_left(nums2, mid_value, l2, r2)
            left_nums_count = small_idx + mid_idx
            print(f"{mid_idx}, {mid_value}, {small_idx}, {left_nums_count}")
            if left_nums_count == total_length // 2:
                if total_length % 2 == 0:
                    if mid_idx == 0:
                        other_med = nums2[small_idx-1]
                    elif small_idx == 0:
                        other_med = nums1[mid_idx-1]
                    else:
                        other_med = max(nums1[mid_idx-1], nums2[small_idx-1])
                    return (mid_value+other_med) / 2
                else:
                    return mid_value
            else:
                if left_nums_count > total_length // 2:
                    r1 = mid_idx
                    # r2 = small_idx
                else:
                    l1 = mid_idx+1
                    # l2 = small_idx

        med_idx = (total_length // 2) - l1
        print(f"{med_idx}")
        med_value = nums2[med_idx]
        if total_length % 2 == 0:
            if med_idx == 0:
                other_med = nums1[l1-1]
            elif l1 == 0:
                other_med = nums2[med_idx-1]
            else:
                other_med = max(nums1[l1-1], nums2[med_idx-1])
            return (med_value+other_med) / 2
        else:
            return med_value


            




