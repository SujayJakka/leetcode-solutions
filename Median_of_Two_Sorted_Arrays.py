class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        arr = []

        target_index = (m + n) // 2

        while len(arr) <= target_index:

            if p1 < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    arr.append(nums1[p1])
                    p1 += 1
                else:
                    arr.append(nums2[p2])
                    p2 += 1

            elif p1 < m:
                arr.append(nums1[p1])
                p1 += 1
            
            else:
                arr.append(nums2[p2])
                p2 += 1
        
        if (m + n) % 2 == 1:
            return arr[-1]
        else:
            return (arr[-1] + arr[-2]) / 2
