class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            
            arr1 = merge_sort(arr[:mid])
            arr2 = merge_sort(arr[mid:])

            ptr_1, ptr_2 = 0, 0

            for i in range(len(arr)):

                if ptr_1 == len(arr1):
                    arr[i] = arr2[ptr_2]
                    ptr_2 += 1
                    continue
                if ptr_2 == len(arr2):
                    arr[i] = arr1[ptr_1]
                    ptr_1 += 1
                    continue

                if arr1[ptr_1] <= arr2[ptr_2]:
                    arr[i] = arr1[ptr_1]
                    ptr_1 += 1
                else:
                    arr[i] = arr2[ptr_2]
                    ptr_2 += 1
            
            return arr
        
        return merge_sort(nums)

        