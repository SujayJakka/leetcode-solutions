class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        ptr_1, ptr_2, arr_ptr = m - 1, n - 1, m + n - 1

        while ptr_2 >= 0:
            if ptr_1 >= 0 and nums1[ptr_1] > nums2[ptr_2]:
                nums1[arr_ptr] = nums1[ptr_1]
                ptr_1 -= 1
            else:
                nums1[arr_ptr] = nums2[ptr_2]
                ptr_2 -= 1
            
            arr_ptr -= 1

        return nums1
