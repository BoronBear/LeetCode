from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2.0
            else:
                return nums2[len(nums2) // 2]
        
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2.0
            else:
                return nums1[len(nums1) // 2]
        
        # Starting indices
        i, j = (len(nums1)) // 2, (len(nums2)) // 2
        
        # Two odd length arrays, increment by one to keep i+j at the right level
        if (len(nums1) % 2) + (len(nums2) % 2) == 0:
            if i != 0:
                i -= 1
            else:
                j -= 1
             
        
        increment = min(len(nums1), len(nums2))

        i1_counter = 0
        
        while increment > 1:
            if nums1[i] >= nums2[j]:
                increment = min(min((increment + 1) // 2, i), len(nums2) - j - 1)
                i -= increment
                j += increment
            else:
                increment = min(min((increment + 1) // 2, j), len(nums1) - i - 1)
                i += increment
                j -= increment
                
            if increment <= 1:
                i1_counter += 1
                
        i_smaller = nums1[i] <= nums2[j]
        
        if (len(nums1) + len(nums2)) % 2 == 0:
            if i_smaller:
                if j == 0:
                    smaller_num = nums1[i]
                else:
                    smaller_num = max(nums1[i], nums2[j - 1])
                if i == len(nums1) - 1:
                    larger_num = nums2[j]
                else:
                    larger_num = min(nums1[i + 1], nums2[j])
                return (smaller_num + larger_num) / 2.0
            else:
                if i == 0:
                    smaller_num = nums2[j]
                else:
                    smaller_num = max(nums2[j], nums1[i - 1])
                if j == len(nums2) - 1:
                    larger_num = nums1[i]
                else:
                    larger_num = min(nums2[j + 1], nums1[i])
                return (smaller_num + larger_num) / 2.0
                
        else:
            if i_smaller:
                if j == 0:
                    return nums1[i]
                else:
                    return max(nums2[j-1], nums1[i])
            else:
                if i == 0:
                    return nums2[j]
                else:
                    return max(nums1[i-1], nums2[j])
            
        