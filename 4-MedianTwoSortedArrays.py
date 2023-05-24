from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mini = 0
        nums3 = []
        for index, num1 in enumerate(nums1):
            if num1 < nums2[index]:
                nums3.append(num1)
            else:
                nums3.append(nums2[index])
        
        return nums3